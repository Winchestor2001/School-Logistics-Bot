from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from keyboards.inline_btns import tariff_btn, back_to_tariffs_btn
from utils.json_convertor import load_json

router = Router()


@router.message(F.text == "💰 Тарифы")
async def show_tariff_handler(message: Message):
    tariff_data = load_json("tariff_plan.json")
    btn = await tariff_btn(tariff_data['tariffs'])
    await message.answer(text="Выберите тариф:", reply_markup=btn)


@router.callback_query(F.data.startswith("tariff"))
async def show_tariff_detail_handler(c: CallbackQuery):
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

    btn = await back_to_tariffs_btn()
    await c.message.edit_text(text=tariff_text, reply_markup=btn)


@router.callback_query(F.data == "back_to_tariffs")
async def back_handler(c: CallbackQuery):
    await c.message.delete()
    tariff_data = load_json("tariff_plan.json")
    btn = await tariff_btn(tariff_data['tariffs'])
    await c.message.answer(text="Выберите тариф:", reply_markup=btn)
