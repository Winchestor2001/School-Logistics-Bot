from aiogram import Router, F
from aiogram.types import Message
from utils.json_convertor import load_json

router = Router()


@router.message(F.text == "⭐ Отзывы")
async def show_tariff_handler(message: Message):
    testimonials = load_json("testimonials.json")['testimonials']
    await message.answer(text="<b>Отзывы людей, прошедших обучение:</b>")
    for n, testimonial in enumerate(testimonials, 1):
        await message.answer(text=f"<a href='{testimonial}'>Видео {n}</a>")
