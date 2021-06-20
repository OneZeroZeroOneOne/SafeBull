from aiogram import types
from database.db_worker import DBWorker
from loguru import logger
from config import texts, Lang
from aiogram.dispatcher import FSMContext
from handlers.keybs.simple_text import simple_text
from handlers.fsm.main_form import MainForm


async def ref(
    message: types.Message, user: dict, db_worker: DBWorker, _: dict, state: FSMContext
):
    await message.answer(
        _["ref"].format(
            "https://t.me/"
            + (await message.bot.get_me()).username
            + f"?start={message.from_user.id}"
        ),
    )
