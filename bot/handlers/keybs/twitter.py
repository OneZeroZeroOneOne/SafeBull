from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.callback_data import CallbackData  

def twitter_keyb(url: str):
    keyb = InlineKeyboardMarkup()
    keyb.add(InlineKeyboardButton("Twitter", url=url))
    return keyb