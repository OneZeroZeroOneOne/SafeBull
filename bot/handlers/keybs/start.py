from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


def start_keyb(urls, bance, output, ref):
    keyb = ReplyKeyboardMarkup(resize_keyboard=True)
    keyb.row(KeyboardButton(urls), KeyboardButton(bance))
    keyb.add(KeyboardButton(output), KeyboardButton(ref))
    return keyb