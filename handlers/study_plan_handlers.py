from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from keyboards.inline_btns import module_btn, module_lessons_btn, back_to_module_lesson_btn
from utils.context_maker import lessons_context
from utils.json_convertor import load_json

router = Router()


@router.message(F.text == "📚 Программа")
async def show_study_handler(message: Message):
    modules_data = load_json("study_plan.json")
    btn = await module_btn(modules_data)
    await message.answer(text="Выберите модуль:", reply_markup=btn)


@router.callback_query(F.data.startswith("module"))
async def show_module_lessons_callback(c: CallbackQuery):
    module_id = c.data.split(":")[-1]
    modules_data = load_json("study_plan.json")
    lessons = None
    for item in modules_data['modules']:
        if item['module_id'] == int(module_id):
            lessons = item['lessons']
            break

    btn = await module_lessons_btn(lessons)
    await c.message.edit_text(text="Выберите урок:", reply_markup=btn)


@router.callback_query(F.data == "back")
async def back_callback(c: CallbackQuery):
    await c.message.delete()
    await show_study_handler(c.message)


@router.callback_query(F.data.startswith("lesson"))
async def show_lesson_callback(c: CallbackQuery):
    lesson_id = c.data.split(":")[-1]
    modules_data = load_json("study_plan.json")
    lesson_data = None
    module_id = None
    for item in modules_data['modules']:
        for lesson in item['lessons']:
            if lesson['lesson_number'] == int(lesson_id):
                module_id = item['module_id']
                lesson_data = lesson
                break

    btn = await back_to_module_lesson_btn(module_id)
    context = await lessons_context(lesson_data)
    await c.message.edit_text(text=context, reply_markup=btn)
