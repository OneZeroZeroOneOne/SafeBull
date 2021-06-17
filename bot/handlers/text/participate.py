from aiogram import types
from database.db_worker import DBWorker
from aiogram.dispatcher import FSMContext
from handlers.keybs.simple_text import simple_text
from handlers.fsm.main_form import MainForm

async def participate(message: types.Message, user: dict, db_worker: DBWorker, _: dict, state: FSMContext):
    await MainForm.accept_rule.set()
    await message.answer(_["accept_rule"], reply_markup=simple_text(_["accept_rule_button"]))
