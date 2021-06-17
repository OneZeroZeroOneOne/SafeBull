from handlers.keybs.subscribe import subscribe
from aiogram import types
from database.db_worker import DBWorker
from aiogram.dispatcher import FSMContext
from handlers.keybs.simple_text import simple_text
from handlers.fsm.main_form import MainForm
from config import groups

async def confirm_captcha(message: types.Message, user: dict, db_worker: DBWorker, _: dict, state: FSMContext):
    if message.text.isnumeric():
        if int(message.text) == (await state.get_data())["confirm_captcha"]:
            await db_worker.set_confirm_captcha(message.from_user.id)
            await MainForm.set_bep_20.set()
            await message.answer("set_bep_20")
        else:
            if (await state.get_data())["caption_attempt"] == 1:
                await state.finish()
                await db_worker.ban_user(message.from_user.id)
                await message.answer(_["you_was_be_banned"])
            else:
                await state.update_data(caption_attempt=(await state.get_data())["caption_attempt"] - 1)
                await message.answer(_["wrong_captcha_answer"].format((await state.get_data())["caption_attempt"]))
    else:
        await message.answer(_["answer_captcha_is_number"])
