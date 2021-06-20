from handlers.keybs.start import start_keyb
from utils.validate_bep_20 import validate_bep_20
from aiogram import types
from database.db_worker import DBWorker
from loguru import logger
from handlers.fsm.lang import SelectLang
from handlers.keybs.select_lang import select_lang
from config import texts

async def start_new_user(message: types.Message, user: dict, db_worker: DBWorker, _: dict):
    args = message.get_args()
    if user['refferrer_id'] == None:
        await db_worker.add_refferrer_id(message.from_user.id, int(args) if args and args.isnumeric() else 0)
    await SelectLang.select_lang.set()
    await message.answer(_["select_lang"], reply_markup=select_lang([i['lang_name'] for i in texts.values()]))



async def start_old_user(message: types.Message, user, db_worker: DBWorker, _: dict):
    await message.answer(_["start_screen"].format(
        message.from_user.first_name,
        "✅" if message.conf["in_groups"] else "❌",
        "✅" if validate_bep_20(" " if user['bep_address'] == None else user['bep_address']) else "❌",
        user['bep_address'],
        "https://t.me/" + (await message.bot.get_me()).username +f"?start={message.from_user.id}",
        user['tokens']),
        reply_markup=start_keyb(_['balance_button'], _["sot_network_button"] ,_['tokens_output_button'], _["ref_button"])
        )
