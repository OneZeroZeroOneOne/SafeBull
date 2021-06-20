from aiogram import types
from aiogram.types.input_file import InputFile
from database.db_worker import DBWorker
from loguru import logger
from config import texts, Lang
from aiogram.dispatcher import FSMContext
from handlers.keybs.simple_text import simple_text
from handlers.fsm.main_form import MainForm

async def select_lang(message: types.Message, user: dict, db_worker: DBWorker, _: dict, state: FSMContext):
    for key, val in texts.items():
        if val['lang_name'] == message.text:
            lang_id = Lang[key].value
            _ = texts[key]
            await db_worker.set_user_lang(lang_id, message.from_user.id)
    await state.finish()
    await MainForm.participate.set()
    await message.answer_photo(InputFile("participate.jpg", filename="participate.jpg"), caption=_["participate"].format(message.from_user.first_name), reply_markup=simple_text(_["participate_button"]))
