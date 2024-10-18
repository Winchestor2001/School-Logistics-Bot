from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


async def module_btn(modules):
    btn = InlineKeyboardBuilder()

    btn.add(
        *[
            InlineKeyboardButton(text=f"Модуль {module['module_number']}",
                                 callback_data=f"module_{module['module_number']}") for module in modules
        ]
    )
    btn.adjust(2)
    return btn.as_markup()
