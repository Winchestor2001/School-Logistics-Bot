from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from keyboards.inline_btns import help_btn
from keyboards.reply_btns import start_command_btn

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    context = ("<b>Добро пожаловать в онлайн-школу практического обучения логистике! 🚛📦</b>\n\n"
               "Мы поможем вам освоить все необходимые навыки для успешной работы в сфере логистики.\n\n"
               "<b>📚 Что предлагает наша школа?</b>\n"
               "Практические курсы с реальными кейсами\n"
               "Доступ к профессиональным материалам и экспертизе\n"
               "Индивидуальная поддержка и консультации")
    btn = await start_command_btn()
    await message.answer(context, reply_markup=btn)


@router.message(Command('help'))
async def help_command(message: Message):
    context = (
        "<b>Возникли проблемы с оплатой или вам не одобрили рассрочку?</b>\n"
        "<em>Напишите нам в удобный для вас мессенджер, и мы обязательно вам поможем!</em>"
    )
    btn = await help_btn()
    await message.answer(text=context, reply_markup=btn)
