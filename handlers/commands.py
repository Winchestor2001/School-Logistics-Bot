from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.reply_btns import start_command_btn

router = Router()


@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    context = ("<b>Добро пожаловать в онлайн-школу практического обучения логистике! 🚛📦</b>\n\n"
               "Мы поможем вам освоить все необходимые навыки для успешной работы в сфере логистики.\n\n"
               "<b>📚 Что предлагает наша школа?</b>\n"
               "Практические курсы с реальными кейсами\n"
               "Доступ к профессиональным материалам и экспертизе\n"
               "Индивидуальная поддержка и консультации")
    btn = await start_command_btn()
    await message.answer(context, reply_markup=btn)
    await state.clear()
