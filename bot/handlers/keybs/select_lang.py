

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.callback_data import CallbackData  

cancel_search_cb = CallbackData("cancel_search_cb", "search_id")


def select_lang(langs):
    keyb = ReplyKeyboardMarkup(resize_keyboard=True)
    for lang in langs:
        keyb.add(KeyboardButton(lang))
    return keyb


