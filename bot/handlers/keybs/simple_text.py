from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


def simple_text(text):
    keyb = ReplyKeyboardMarkup(resize_keyboard=True)
    keyb.add(KeyboardButton(text))
    return keyb