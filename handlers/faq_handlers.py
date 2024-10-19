from aiogram import Router, F
from aiogram.types import Message
from utils.json_convertor import load_json

router = Router()


@router.message(F.text == "❓ Faq")
async def show_faq_handler(message: Message):
    faqs = load_json("faq.json")['faq']
    faq_text = "<b>Ответы на вопросы:</b>\n\n"

    for i, faq in enumerate(faqs, 1):
        faq_text += f"<b>{i}) {faq['question']}</b>\n<em>{faq['answer']}</em>\n\n"

    await message.answer(text=faq_text)
