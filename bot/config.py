import datetime
import os
from enum import Enum

bot_token = os.environ.get("bot_token")

postgresql = os.environ.get("db_conn_str")


groups = []

token_for_refferral = 200000

texts = {
    'ru': {
        "hello": "Привет",
        "select_lang": "<b>Выберите язык</b>",
        "lang_name": "Русский🇷🇺",
        "participate_button": "Участвовать в Airdrop",
        "participate": """Привет, {}, я  SafeBull AirDrop Bot 🚀🤝 

✅ Чтобы получить монеты в раздаче вам нужно выполнить несколько заданий

🔸 За выполнение всех заданий вы получите 300.000 токенов SAFEBULL

⭐️ За приглашенного друга вы получите 200.000 токенов SAFEBULL 

Нажми "Участвовать в Airdrop" чтобы продолжить""",
        "accept_rule": """📘 Участвуя, вы соглашаетесь на условия и правила Раздачи SafeBull 

👨‍💻 Пожалуйста, прочитайте внимательно👩‍💻

❗️Выполнив все задания вы получите максимальное количество токенов в качестве вознаграждения, если вы не выполните одно из условий - тогда получить награду будет невозможно.

❗️Выполнение заданий строго проверятся и если одно из условий не будет выполнено, токены SAFEBULL не будут начислены. Мы хотим чтобы вы получили максимальное количество токенов, поэтому убедительно просим вас выполнять все задания и оставаться подписанными на наши социальные сети до окончания Airdrop. Если вы или ваш реферал отпишется до окончания раздачи - награда будет вычтена с вашего баланса! 

Нажмите "Согласен" если вы принимаете условия и правила Airdrop.""",
        "accept_rule_button": "Согласен",
        "captcha": """Для того чтобы продолжить,
пожалуйста ответь на этот
математический вопрос. Это
нужно для того чтобы понять
человек ты или бот.
У тебя осталось 3 попытки""",
        "answer_captcha_is_number": "Вы должны ввести число",
        "wrong_captcha_answer": "Неправильный ответ, осталось попыток: {}",
        "you_was_be_banned": "Вы были забанены, бот больше не будет вам отвечать",
        "check_subscribe_button": "Подписался",
        "subscribe_groups": """<b>☑️ Подпишитесь на наш телеграм канал
☑️ Подпишитесь на наш телеграм чат</b>""",
        "subscribe_check_false": "Необходимо подписатся на все каналы и группы",
        "set_bep_20": """Введи свой адрес кошелька BEP-20
(binance smart chain):
⚙️Адрес должен начинаться с 0х
⚙️Пример: 0xfa344c08c93066a4d6266063c6ebc63925a18467""",
        "invalid_bep_address": "<b>Неверный формат!</b> Пожалуйста, введите адрес еще раз",
        'add_token_for_invite_user': 'Вам были начислены {} токен(a/ов) за приглощение юзера {}',
        "start_screen": """Спасибо, {}, что принял участие в Airdrop SafeBull
Ваши данные:
{}Вступил в телеграм канал/чат
{}BEP-20 адресс: {}

Не забывайте: 
🔸 Оставайтесь в телеграм канале
🔸 Будьте подписаны на наши социальные сети

<b>Ваша уникальная ссылка для приглашения друзей:</b> {}

Делитесь или пересылайте свою ссылку, получайте 200.000 токенов SAFEBULL  за каждого реферала👬
Они также должны участвовать в Airdrop и принять условия для получения награды! Пользователи, которые будут замечены в мошенничестве, будут заблокированы без возможности вывода средств.""",
        "tokens_output_button": "💰Вывод",
        "tokens_output": "Напишите целое количество SAFEBULL которое вы хотите вывести.\n На вашем счету <b>{}</b> SAFEBULL.",
        "please_write_number": "🤦🏻<b>Введите число!</b>",
        "thnx_for_subscribes": "🎉Спасибо за подписку на наши ресурсы!",
        "output_order_created": "Заказ на вывод SafeBull был создан\n<b>Заказ №: {}</b>",
        "order_alr_exist": "⏱У вас уже есть заказ на вывод SafeBull, подождите пока ваш заказ одобрят, после чего вы сможете создать новый заказ",
        "cancel_button": "❌Отменить❌",
        "cancel": "✅Отменено✅",
        "not_enough_money": "🚧Не достаточно SafeBull на вашем счету",
        "twitter_subscribe": "<b>☑️ Подпишитесь на наш Twitter</b>",
        "balance": """💰 Всего: {} SAFEBULL 
💵 Бонус за рефералов: {} SAFEBULL 
Рефералов: {} """,
        "balance_button": "Баланс 💰",
        "sot_network_button": "Соц. сети 📤",
        "sot_network": """<a href="https://t.me/joinchat/DeOkSTknKgs4NDMy">SafeBull Telegram channel</a>
<a href="https://t.me/SafeBullChat_ru">SafeBull Telegram чат</a>
<a href="http://twitter.com/SafeBull1">SafeBull Twitter</a>
<a href="https://safe-bull.com/#faq">SafeBull Веб-сайт</a>
<a href="https://www.instagram.com/safe_bull">SafeBull Instagram</a>
<a href="https://www.reddit.com/r/SafeBull_Official/">SafeBull Reddit</a>""",
        "ref_button": "Реферальная ссылка 👥",
        "ref": """Ваша уникальная реферальная ссылка:
{}

Поделитесь и перешлите реферальную ссылку и получите 200.000 SAFEBULL с каждого реферала!

Делитесь или пересылайте свою ссылку, получайте 200.000 токенов SAFEBULL за каждого реферала👬
Они также должны участвовать в Airdrop и принять условия для получения награды! Пользователи, которые будут замечены в мошенничестве, будут заблокированы без возможности вывода средств."""
    },
    'en': {
        "hello": "hello",
        "select_lang": "<b>Select you language</b>",
        "lang_name": "English🇺🇸",
        "participate": """Hi {}, I'm SafeBull AirDrop Bot 🚀🤝

✅ To get coins in the distribution you need to complete several tasks

🔸 For completing all tasks you will receive 300,000 SAFEBULL tokens

⭐️ For an invited friend, you will receive 200,000 SAFEBULL tokens

Click "Participate in Airdrop" to continue""",
        "participate_button": "Participate in Airdrop",
        "accept_rule": """📘 By participating, you agree to the SafeBull Giveaway Terms and Conditions

👨‍💻 Please read carefully👩‍💻

❗️ After completing all the tasks, you will receive the maximum number of tokens as a reward, if you do not fulfill one of the conditions, then it will be impossible to receive the reward.

❗️The completion of tasks is strictly checked and if one of the conditions is not met, SAFEBULL tokens will not be credited. We want you to get the maximum number of tokens, so we kindly ask you to complete all tasks and stay subscribed to our social networks until the end of the Airdrop. If you or your referral unsubscribe before the end of the distribution, the reward will be deducted from your balance!

Click “Agree” if you accept the terms and conditions of the Airdrop.""",
        "accept_rule_button": "Agree",
        "captcha": """To continue,
please answer this
math question. it
you need to understand
you are a human or a bot.
You have 3 attempts left""",
        "answer_captcha_is_number": "You must enter a number",
        "wrong_captcha_answer": "Wrong answer, attempts left: {}",
        "you_was_be_banned": "You have been banned, the bot will no longer answer you",
        "check_subscribe_button": "Subscribed",
        "subscribe_groups": """<b>☑️ Subscribe to our telegram channel
☑️ Subscribe to our telegram chat</b>""",
        "subscribe_check_false": "You need to subscribe to all channels and groups",
        "set_bep_20": """Enter your BEP-20 wallet address
(binance smart chain):
⚙️Address must start with 0x
⚙️Example: 0xfa344c08c93066a4d6266063c6ebc63925a18467""",
        "invalid_bep_address": "<b>Wrong format!</b> Please enter the address again",
        'add_token_for_invite_user': 'You were credited with {} token(s) for attracting a user {}',
        "start_screen": """Thank you {} for participating in the SafeBull Airdrop
Your data:
{} Joined telegram channel/chat
{} BEP-20 Address: {}

Do not forget:
🔸 Stay in the telegram channel
🔸 Be subscribed to our social networks

<b>Your unique link for inviting friends:</b> {}

Share or forward your link, get 200,000 SAFEBULL tokens for each referral👬
They must also participate in the Airdrop and agree to receive the reward! Users who are found to be fraudulent will be blocked without the possibility of withdrawing funds.""",
        "tokens_output_button": "💰Output",
        "tokens_output": "Write the whole amount of SAFEBULL you want to withdraw.\nYour account is <b>{}</b> SAFEBULL.",
        "please_write_number": "🤦🏻<b>Enter a number!</b>",
        "thnx_for_subscribes": "🎉Thank you for subscribing to our resources!",
        "output_order_created": "SafeBull withdrawal order has been created\n<b>Order №: {}</b>",
        "order_alr_exist": "⏱You already have a SafeBull withdrawal order, wait until your order is approved, after which you can create a new order",
        "cancel_button": "❌Cancel❌",
        "cancel": "✅Canceled✅",
        "not_enough_money": "🚧Not enough SafeBull in your account",
        "twitter_subscribe": "<b>☑️ Follow us on Twitter</b>",
        "balance": """💰 Total: {} SAFEBULL
💵 Bonus for referrals: {} SAFEBULL
Referrals: {}""",
        "balance_button": "Balance 💰",
        "sot_network_button": "Social networks 📤",
        "sot_network": """<a href="https://t.me/joinchat/DeOkSTknKgs4NDMy">SafeBull Telegram channel</a>
<a href="https://t.me/SafeBullChat_ru">SafeBull Telegram chat</a>
<a href="http://twitter.com/SafeBull1">SafeBull Twitter</a>
<a href="https://safe-bull.com/#faq">SafeBull Web-site</a>
<a href="https://www.instagram.com/safe_bull">SafeBull Instagram</a>
<a href="https://www.reddit.com/r/SafeBull_Official/">SafeBull Reddit</a>""",
        "ref_button": "Referral link 👥",
        "ref": """Your unique referral link:
{}

Share and forward your referral link and get 200.000 SAFEBULL from each referral!

Share or forward your link, get 200,000 SAFEBULL tokens for each referral👬
They must also participate in the Airdrop and agree to receive the reward! Users who are found to be fraudulent will be blocked without the possibility of withdrawing funds."""
    }
}


group_leave_timeout_sec = 60*10


class Lang(Enum):
    ru = 1
    en = 2

Lang

DEFAULT_LANG = Lang.ru