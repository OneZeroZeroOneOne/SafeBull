from aiogram import types
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from database.db_worker import DBWorker
from aiogram.dispatcher import FSMContext
from aiogram.types.input_file import InputFile
from handlers.keybs.simple_text import simple_text
from handlers.fsm.main_form import MainForm
from PIL import Image, ImageDraw, ImageFont
import random
import os


async def accept_rule(message: types.Message, user: dict, db_worker: DBWorker, _: dict, state: FSMContext):
    await db_worker.set_accept_rule(message.from_user.id)
    await MainForm.confirm_captcha.set()
    a = random.randint(0, 100)
    b = random.randint(0, a)
    text = f"{a} - {b}"
    filename = text_on_img(f"{message.from_user.id}_captcha.png", text, size=300)
    await state.update_data(confirm_captcha=a-b)
    await state.update_data(caption_attempt=3)
    await message.answer_photo(InputFile(filename, filename=filename), caption=_["captcha"], reply_markup=ReplyKeyboardRemove())
    os.remove(filename)



def text_on_img(filename, text, size=12):
    fnt = ImageFont.truetype('arial.ttf', size)
    image = Image.new(mode = "RGB", size = (int(size/2)*len(text),size+50), color = "red")
    draw = ImageDraw.Draw(image)
    draw.text((10,10), text, font=fnt, fill=(255,255,0))
    image.save(filename)
    return filename