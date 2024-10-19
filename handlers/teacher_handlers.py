from aiogram import Router, F
from aiogram.types import Message
from utils.json_convertor import load_json

router = Router()


@router.message(F.text == "👨‍🏫 Преподаватели")
async def show_teachers_handler(message: Message):
    teachers = load_json("teachers.json")['teachers']
    await message.answer(text="<b>Наши преподаватели:</b>")
    for teacher in teachers:
        context = f"<b>{teacher['name']}</b>\n<em>{teacher['description']}</em>"
        await message.answer_photo(photo=teacher['photo_url'], caption=context)
