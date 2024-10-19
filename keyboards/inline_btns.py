from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


async def module_btn(modules):
    btn = InlineKeyboardBuilder()
    btn.add(
        *[
            InlineKeyboardButton(text=module['module_name'],
                                 callback_data=f"module:{module['module_id']}") for module in modules['modules']
        ]
    )
    btn.adjust(2)
    return btn.as_markup()


async def module_lessons_btn(lessons):
    btn = InlineKeyboardBuilder()
    btn.add(
        *[
            InlineKeyboardButton(text=f"Урок {lesson['lesson_number']}",
                                 callback_data=f"lesson:{lesson['lesson_number']}") for lesson in lessons
        ],
        InlineKeyboardButton(text="🔙 Назад", callback_data="back")
    )
    btn.adjust(2)
    return btn.as_markup()


async def back_to_module_lesson_btn(module_id):
    btn = InlineKeyboardBuilder()
    btn.add(
        InlineKeyboardButton(text="🔙 Назад", callback_data=f"module:{module_id}")
    )
    return btn.as_markup()


async def tariff_btn(tariffs):
    btn = InlineKeyboardBuilder()
    btn.add(
        *[
            InlineKeyboardButton(text=tariffs[tariff]['name'],
                                 callback_data=f"tariff:{tariff}") for tariff in tariffs.keys()
        ]
    )
    btn.adjust(1)
    return btn.as_markup()


async def back_to_tariffs_btn():
    btn = InlineKeyboardBuilder()
    btn.add(
        InlineKeyboardButton(text="🔙 Назад", callback_data=f"back_to_tariffs")
    )
    return btn.as_markup()


async def help_btn():
    btn = InlineKeyboardBuilder()
    btn.add(
        InlineKeyboardButton(text="💬 Telegram", url="https://t.me/Dimonkite"),
        InlineKeyboardButton(text="📱 WhatsApp", url="https://wa.me/79657267878")
    )
    return btn.as_markup()