from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.callback_data import CallbackData  

check_subscribe_cb = "check_subscribe_cb"

def subscribe(groups: dict, check_button_title):
    keyb = InlineKeyboardMarkup()
    for key, val in groups.items():
        keyb.add(InlineKeyboardButton(key, url=val))
    keyb.add(InlineKeyboardButton(check_button_title, callback_data=check_subscribe_cb))
    return keyb