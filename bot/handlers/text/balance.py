from aiogram import types
from database.db_worker import DBWorker
from loguru import logger
from config import texts, Lang
from aiogram.dispatcher import FSMContext
from handlers.keybs.simple_text import simple_text
from handlers.fsm.main_form import MainForm


async def balance(
    message: types.Message, user: dict, db_worker: DBWorker, _: dict, state: FSMContext
):
    accruals = await db_worker.get_invite_user_accruals(message.from_user.id)
    rules_tokens = await db_worker.get_rules_tokens(message.from_user.id)
    for_ref_tokens = 0
    for i in accruals:
        for_ref_tokens += i["tokens"]
    await message.answer(
        _["balance"].format(
            user["tokens"],
            rules_tokens['tokens'] if rules_tokens else 0 
            ,for_ref_tokens, len(accruals))
    )
