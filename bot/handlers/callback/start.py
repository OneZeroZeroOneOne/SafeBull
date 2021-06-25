
from aiogram.dispatcher.storage import FSMContext
from handlers.keybs.select_lang import select_lang
from handlers.fsm.lang import SelectLang
from aiogram import types
import typing

from aiogram.types import message
from database.db_worker import DBWorker
from config import groups, token_for_refferral, texts
from handlers.keybs.subscribe import subscribe


async def start_new_user_cb(query: types.CallbackQuery, user: dict, db_worker: DBWorker, _: dict, state: FSMContext):
    await state.finish()
    await SelectLang.select_lang.set()
    await query.message.answer(_["select_lang"], reply_markup=select_lang([i['lang_name'] for i in texts.values()]))