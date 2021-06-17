from utils.validate_bep_20 import validate_bep_20
from aiogram import types
from database.db_worker import DBWorker
from aiogram.dispatcher import FSMContext
from handlers.keybs.simple_text import simple_text
from handlers.fsm.main_form import MainForm
from config import groups
from handlers.keybs.subscribe import subscribe

async def set_bep_20(message: types.Message, user: dict, db_worker: DBWorker, _: dict, state: FSMContext):
    if validate_bep_20(message.text):
        await db_worker.set_bep_address(message.text, message.from_user.id)
        await state.finish()
        chat_name_url = {}
        for group_id in groups:
            chat = await message.bot.get_chat(group_id)
            chat_name_url[chat.full_name] = await chat.get_url()
        await message.answer(_["subscribe_groups"], reply_markup=subscribe(chat_name_url, _['check_subscribe_button']))
    else:
        await message.answer(_["invalid_bep_address"])

