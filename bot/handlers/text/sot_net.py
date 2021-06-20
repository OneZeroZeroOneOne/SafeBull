from aiogram import types
from database.db_worker import DBWorker
from aiogram.dispatcher import FSMContext



async def sot_net(message: types.Message, user: dict, db_worker: DBWorker, _: dict, state: FSMContext):
    await message.answer(_["sot_network"], disable_web_page_preview=True)
