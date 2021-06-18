from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.callback_data import CallbackData  

cancel_cb = "cancel_cb"

def cancel(text):
    keyb = InlineKeyboardMarkup()
    keyb.add(InlineKeyboardButton(text, callback_data=cancel_cb))
    return keyb