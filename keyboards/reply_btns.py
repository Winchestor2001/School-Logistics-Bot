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


async def back_btn():
    btn = ReplyKeyboardBuilder()
    btn.row(
        KeyboardButton(text="❌ Отменить покупку")
    )
    return btn.as_markup(resize_keyboard=True)


async def share_phone_number_btn():
    btn = ReplyKeyboardBuilder()
    btn.row(
        KeyboardButton(text="📲 Поделится телефон номером", request_contact=True),
        KeyboardButton(text="❌ Отменить покупку")
    )
    btn.adjust(1)
    return btn.as_markup(resize_keyboard=True)