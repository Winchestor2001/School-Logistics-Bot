from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.inline_btns import module_btn
from utils.json_convertor import load_json

router = Router()


@router.message("📚 Программа")
async def show_study_handler(message: Message):
    modules_data = load_json("study_plan.json")
    btn = await module_btn(modules_data)
    await message.answer(text="Выберите модуль:", reply_markup=btn)

