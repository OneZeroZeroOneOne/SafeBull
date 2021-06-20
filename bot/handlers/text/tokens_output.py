from handlers.keybs.cancel import cancel
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from handlers.keybs.start import start_keyb
from handlers.keybs.subscribe import subscribe
from aiogram import types
from database.db_worker import DBWorker
from aiogram.dispatcher import FSMContext
from handlers.keybs.simple_text import simple_text
from handlers.fsm.tokens_output import TokensOutputForm
from config import groups
from datetime import datetime

async def tokens_output(message: types.Message, user: dict, db_worker: DBWorker, _: dict):
    exist_output = await db_worker.get_tokens_output(user['id'])
    if not exist_output:
        await TokensOutputForm.set_count.set()
        await message.answer(_['tokens_output'].format(user['tokens']), reply_markup=cancel(_['cancel_button']))
    else:
        await message.answer(_["order_alr_exist"], reply_markup=start_keyb(_['balance_button'], _["sot_network_button"] ,_['tokens_output_button'], _["ref_button"]))


async def writed_tokens_output_count(message: types.Message, user: dict, db_worker: DBWorker, _: dict, state: FSMContext):
    if message.text.isnumeric():
        if user['tokens'] >= int(message.text):
            exist_output = await db_worker.get_tokens_output(user['id'])
            if exist_output:
                await message.answer(_["order_alr_exist"], reply_markup=start_keyb(_['balance_button'], _["sot_network_button"] ,_['tokens_output_button'], _["ref_button"]))
                await state.finish()
                return
            await db_worker.minus_user_tokens(user['id'], int(message.text))
            id = await db_worker.add_tokens_output(user['id'], datetime.now(), int(message.text))
            if id:
                await message.answer(_["output_order_created"].format(id), reply_markup=start_keyb(_['balance_button'], _["sot_network_button"] ,_['tokens_output_button'], _["ref_button"]))
            else:
                await message.answer("ERROR oreder not created", reply_markup=start_keyb(_['balance_button'], _["sot_network_button"] ,_['tokens_output_button'], _["ref_button"]))
            await state.finish()
        else:
            await message.answer(_["not_enough_money"], reply_markup=cancel(_['cancel_button']))
    else:
        await message.answer(_['please_write_number'], reply_markup=cancel(_['cancel_button']))
