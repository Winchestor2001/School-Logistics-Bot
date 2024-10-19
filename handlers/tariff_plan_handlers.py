from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.inline_btns import tariff_btn, tariff_detail_btn
from keyboards.reply_btns import back_btn, share_phone_number_btn, start_command_btn
from states.AllStates import BuyTariffState
from utils.json_convertor import load_json

router = Router()


@router.message(F.text == "❌ Отменить покупку")
async def cancel_buy_tariff_handler(message: Message, state: FSMContext):
    await state.clear()
    btn = await start_command_btn()
    await message.answer("❌ Покупка отменена.", reply_markup=btn)


@router.message(F.text == "💰 Тарифы")
async def show_tariff_handler(message: Message):
    tariff_data = load_json("tariff_plan.json")
    btn = await tariff_btn(tariff_data['tariffs'])
    await message.answer(text="Выберите тариф:", reply_markup=btn)


@router.callback_query(F.data.startswith("tariff"))
async def show_tariff_detail_callback(c: CallbackQuery):
    tariff_name = c.data.split(":")[-1]
    tariffs_data = load_json("tariff_plan.json")

    tariff = tariffs_data['tariffs'].get(tariff_name, None)

    if not tariff:
        await c.answer("Тариф не найден. Попробуйте еще раз.", show_alert=True)
        return

    tariff_text = f"<b>{tariff['name']}</b>\n\n"
    tariff_text += f"💸 <b>Скидка:</b> {tariff['discount']}\n\n"
    tariff_text += "📋 <b>Основные преимущества:</b>\n"

    for feature in tariff['features']:
        tariff_text += f"• {feature}\n"

    btn = await tariff_detail_btn()
    await c.message.edit_text(text=tariff_text, reply_markup=btn)


@router.callback_query(F.data == "back_to_tariffs")
async def back_callback(c: CallbackQuery):
    await c.message.delete()
    tariff_data = load_json("tariff_plan.json")
    btn = await tariff_btn(tariff_data['tariffs'])
    await c.message.answer(text="Выберите тариф:", reply_markup=btn)


@router.callback_query(F.data.startswith("buy"))
async def buy_tariff_callback(c: CallbackQuery, state: FSMContext):
    cd = c.data
    if cd == "buy_tariff":
        tariff_status = "💳 Приобрести тариф"
    else:
        tariff_status = "💼 Приобрести в рассрочку"

    btn = await back_btn()
    await state.update_data(tariff_status=tariff_status)
    await c.message.delete()
    await c.message.answer(text="Введите ваше имя:", reply_markup=btn)
    await state.set_state(BuyTariffState.first_name)


@router.message(BuyTariffState.first_name)
async def first_name_state(message: Message, state: FSMContext):
    text = message.text
    await state.update_data(first_name=text)

    btn = await share_phone_number_btn()
    await message.answer(text="📱 Поделитесь телефон номером", reply_markup=btn)
    await state.set_state(BuyTariffState.phone_number)


@router.message(BuyTariffState.phone_number,  F.content_type.in_({'contact'}))
async def phone_number_state(message: Message, state: FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data(phone_number=phone_number)

    btn = await back_btn()
    await message.answer(text="Введите вашу почту:", reply_markup=btn)
    await state.set_state(BuyTariffState.email)


@router.message(BuyTariffState.email)
async def email_state(message: Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    context = f"<b>Имя:</b> {data['first_name']}\n<b>Тел.номер:</b> <code>{data['phone_number']}</code>\n<b>Почта:</b> <code>{text}</code>\n<b>Способ оплаты:</b> <em>{data['tariff_status']}</em>"
    await message.answer(text=context)
    await state.clear()