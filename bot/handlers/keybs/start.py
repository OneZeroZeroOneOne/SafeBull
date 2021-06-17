from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


def start_keyb(info, output):
    keyb = ReplyKeyboardMarkup()
    keyb.add(KeyboardButton(info))
    keyb.add(KeyboardButton(output))
    return keyb