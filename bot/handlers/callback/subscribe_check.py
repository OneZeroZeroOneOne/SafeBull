from handlers.keybs.start import start_keyb
from aiogram import types
import typing

from aiogram.types import message
from database.db_worker import DBWorker
from config import groups, token_for_refferral, token_for_subscribe
from handlers.keybs.subscribe import subscribe
from utils.validate_bep_20 import validate_bep_20
from datetime import datetime



async def subscribe_check_false(
    query: types.CallbackQuery, user: dict, db_worker: DBWorker, _: dict
):
    await query.message.answer(_["subscribe_check_false"])
    chat_name_url = {}
    for group_id in groups:
        chat = await query.bot.get_chat(group_id)
        chat_name_url[chat.full_name] = await chat.get_url()
    await query.message.answer(
        _["subscribe_groups"],
        reply_markup=subscribe(chat_name_url, _["check_subscribe_button"]),
    )


async def subscribe_check_true(
    query: types.CallbackQuery, user: dict, db_worker: DBWorker, _: dict
):
    rules_tokens = await db_worker.get_rules_tokens(query.from_user.id)
    if not rules_tokens:
        await db_worker.add_rules_tokens(query.from_user.id, token_for_subscribe, datetime.now())
        await db_worker.add_token_for_user(query.from_user.id, token_for_subscribe)
    if user["refferrer_id"]:
        accrual = await db_worker.get_invite_accruals(
            query.from_user.id, user["refferrer_id"]
        )
        if not accrual:
            await db_worker.add_invite_accruals(
                user["refferrer_id"], user["id"], datetime.now(), token_for_refferral
            )
            try:
                await db_worker.add_token_for_user(
                    user["refferrer_id"], token_for_refferral
                )
            except:
                pass
            await query.bot.send_message(
                user["refferrer_id"],
                text=_["add_token_for_invite_user"].format(
                    token_for_refferral, query.from_user.full_name
                ),
            )
    await query.message.answer(_["thnx_for_subscribes"])
    await query.message.answer(
        _["start_screen"].format(
            query.from_user.first_name,
            "✅" if query.conf["in_groups"] else "❌",
            "✅"
            if validate_bep_20(
                " " if user["bep_address"] == None else user["bep_address"]
            )
            else "❌",
            user["bep_address"],
            "https://t.me/"
            + (await query.bot.get_me()).username
            + f"?start={query.from_user.id}",
            user["tokens"],
        ),
        reply_markup=start_keyb(_['balance_button'], _["sot_network_button"] ,_['tokens_output_button'], _["ref_button"]),
    )
