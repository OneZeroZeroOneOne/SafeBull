from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


def simple_text(text):
    keyb = ReplyKeyboardMarkup()
    keyb.add(KeyboardButton(text))
    return keyb