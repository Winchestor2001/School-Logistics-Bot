from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton


async def start_command_btn():
    btn = ReplyKeyboardBuilder()
    btn.row(
        KeyboardButton(text="📚 Программа"),
        KeyboardButton(text="💰 Тарифы")
    )
    btn.row(
        KeyboardButton(text="⭐ Отзывы"),
        KeyboardButton(text="👨‍🏫 Преподаватели")
    )
    btn.row(
        KeyboardButton(text="❓ Faq")
    )
    return btn.as_markup(resize_keyboard=True)