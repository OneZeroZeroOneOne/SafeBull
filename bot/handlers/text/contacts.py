from aiogram import types
from database.db_worker import DBWorker
from loguru import logger
from config import texts, Lang
from aiogram.dispatcher import FSMContext
from handlers.keybs.simple_text import simple_text
from handlers.fsm.main_form import MainForm

async def contacts(message: types.Message, user: dict, db_worker: DBWorker, _: dict, state: FSMContext):
    await message.answer(_['owner_contacts'])
