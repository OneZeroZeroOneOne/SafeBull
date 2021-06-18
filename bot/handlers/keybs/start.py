from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


def start_keyb(info, output, kabinet):
    keyb = ReplyKeyboardMarkup(resize_keyboard=True)
    keyb.row(*[KeyboardButton(kabinet), KeyboardButton(info)])
    keyb.add(KeyboardButton(output))
    return keyb