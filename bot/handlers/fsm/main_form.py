
from aiogram.dispatcher.filters.state import State, StatesGroup


class MainForm(StatesGroup):
    participate = State()
    accept_rule = State()
    confirm_captcha = State()
    set_bep_20 = State()

    
