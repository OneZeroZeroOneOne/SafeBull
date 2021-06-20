
from handlers.text.ref import ref
from handlers.text.sot_net import sot_net
from handlers.text.balance import balance
from handlers.callback.cancel import cancel
from handlers.text.tokens_output import tokens_output, writed_tokens_output_count
from handlers.callback.start import start_new_user_cb
from handlers.text.set_bep_20 import set_bep_20
from handlers.callback.subscribe_check import subscribe_check_false, subscribe_check_true
from handlers.text.confirm_captcha import confirm_captcha
from handlers.text.accept_rule import accept_rule
from handlers.text.participate import participate
from handlers.fsm.main_form import MainForm
from handlers.text.lang import select_lang
from aiogram import Bot, Dispatcher
from handlers.text.start import start_new_user, start_old_user
from config import texts
from handlers.fsm.lang import SelectLang
from handlers.keybs.subscribe import check_subscribe_cb
from handlers.fsm.tokens_output import TokensOutputForm
from handlers.keybs.cancel import cancel_cb

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_new_user, lambda msg: msg.conf["has_rights"] == False, commands=['start'])
    dp.register_message_handler(start_new_user, lambda msg: msg.conf["has_rights"] == False)
    dp.register_callback_query_handler(start_new_user_cb, lambda msg: msg.conf["has_rights"] == False)
    

    dp.register_message_handler(select_lang, lambda msg: msg.text in [i['lang_name'] for i in texts.values()], state=SelectLang.select_lang)
    dp.register_message_handler(participate, lambda msg: msg.text in [i['participate_button'] for i in texts.values()], state=MainForm.participate)
    dp.register_message_handler(accept_rule, lambda msg: msg.text in [i['accept_rule_button'] for i in texts.values()], state=MainForm.accept_rule)
    dp.register_message_handler(confirm_captcha, state=MainForm.confirm_captcha)
    dp.register_message_handler(set_bep_20, state=MainForm.set_bep_20)
    

    dp.register_message_handler(start_old_user, lambda msg: msg.conf["has_rights"] == True, commands=['start'])
    dp.register_message_handler(tokens_output, lambda msg: msg.text in [i['tokens_output_button'] for i in texts.values()] and msg.conf["has_rights"] == True and msg.conf["in_groups"] == True,)
    dp.register_message_handler(writed_tokens_output_count, state=TokensOutputForm.set_count)
    dp.register_message_handler(balance, lambda msg: msg.text in [i['balance_button'] for i in texts.values()])
    dp.register_message_handler(sot_net, lambda msg: msg.text in [i['sot_network_button'] for i in texts.values()])
    dp.register_message_handler(ref, lambda msg: msg.text in [i['ref_button'] for i in texts.values()])
    

    dp.register_callback_query_handler(subscribe_check_false, lambda msg: msg.data == check_subscribe_cb and msg.conf["has_rights"] == True and msg.conf["in_groups"] == False)
    dp.register_callback_query_handler(subscribe_check_true, lambda msg: msg.data == check_subscribe_cb and msg.conf["has_rights"] == True and msg.conf["in_groups"] == True)
    dp.register_callback_query_handler(cancel, lambda msg: msg.data == cancel_cb, state='*')

    