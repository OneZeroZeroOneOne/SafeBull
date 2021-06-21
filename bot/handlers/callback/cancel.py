
from handlers.keybs.start import start_keyb
from aiogram.dispatcher.storage import FSMContext
from handlers.keybs.select_lang import select_lang
from handlers.fsm.lang import SelectLang
from aiogram import types
import typing

from aiogram.types import message
from database.db_worker import DBWorker
from config import groups, token_for_refferral, texts
from handlers.keybs.subscribe import subscribe


async def cancel(query: types.CallbackQuery, user: dict, db_worker: DBWorker, _: dict, state: FSMContext):
    await state.finish()
    await query.message.delete()
    await query.message.answer(_["cancel"], reply_markup=start_keyb(_['balance_button'], _["sot_network_button"] ,_['tokens_output_button'], _["ref_button"]))