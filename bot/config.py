import datetime
import os
from enum import Enum

bot_token = os.environ.get("bot_token")

postgresql = os.environ.get("db_conn_str")



groups = [-1001433489060]

token_for_refferral = 200000

texts = {
    'ru': {
        "hello": "Привет",
        "select_lang": "Выберите язык",
        "lang_name": "Русский",
        "participate_button": "Принять участие",
        "participate": "Хотите принять участие?",
        "accept_rule": "Согласитесь с нашими правилами",
        "accept_rule_button": "Согласен",
        "captcha": "Капча",
        "answer_captcha_is_number": "Вы должны ввести число",
        "wrong_captcha_answer": "неправильный ответ, осталось попыток {}",
        "you_was_be_banned": "Вы были забанены, бот больше не будет вам отвечать",
        "check_subscribe_button": "Подписался",
        "subscribe_groups": "Подпишитесь на наши ресурсы",
        "subscribe_check_false": "Необходимо подписатся на все каналы и группы",
        "set_bep_20": "Введите свой DEB 20 адресс",
        "invalid_bep_address": "некорректный BEP адресс",
        'add_token_for_invite_user': 'Вам были начислены {} токен(a/ов) за приглощение юзера {}',
        "start_screen": "Ваши детали:\n{} подписаны на канал/группу\n{} BEP-20 address - {}\nВаша реферальная ссылка - {}\nНа вашем счету - {} SAFEBULL",
        "owner_contacts_button": "Контакты",
        "owner_contacts": "Здесь должны быть контакты владельцев",
        "tokens_output_button": "Вывод",
        "tokens_output": "Напишите целое количество SAFEBULL которое вы хотите вывести. На вашем счету {} SAFEBULL",
        "please_write_number": "Введите число!",
        "thnx_for_subscribes": "Спасибо что подписались на наши ресурсы",
        "output_order_created": "Заявка на вывод была создана № заявки - {}",
        "order_alr_exist": "У вас уже есть заявка на вывод, подождите пока вашу заявку одобрят, после чего вы сможете подать новую заявку"
    },
    'en': {
         "hello": "hello",
         "select_lang": "Select you language",
         "lang_name": "English",
         "participate": "Participate text",
         "participate_button": "Participate",
         "accept_rule": "accept rule text",
         "accept_rule_button": "Confirm",
         "captcha": "Captcha",
         "answer_captcha_is_number": "answer_captcha_is_number",
         "wrong_captcha_answer": "wrong_captcha_answer {}",
         "you_was_be_banned": "you_was_be_banned",
         "check_subscribe_button": "check_subscribe_button",
         "subscribe_groups": "subscribe_groups",
         "subscribe_check_false": "subscribe_check_false",
         "set_bep_20": "type your set_bep_20 adress",
         "invalid_bep_address": "invalid_bep_address",
         'add_token_for_invite_user': 'added {} tokens to you wallet  for invite user {}',
         "start_screen": "your details:\n{} subscribe on all groups\n{} BEP-20 address - {}\nyour refferal invite address - {}\nwallet score - {} SAFEBULL",
         "owner_contacts_button": "Contacts",
         "owner_contacts": "here will be owner contacts",
         "tokens_output_button": "Output",
         "tokens_output": "type count of SAFEBULL while you want output. You have {} SAFEBULL",
         "already_exist_output_order": "Order of output already exist",
         "please_write_number": "please_write_number",
         "thnx_for_subscribes": "thnx_for_subscribes",
         "output_order_created": "output_order_created {}",
         "order_alr_exist": "order_alr_exist"
    }
}




group_leave_timeout_sec = 60*10


class Lang(Enum):
    ru = 1
    en = 2

Lang

DEFAULT_LANG = Lang.ru