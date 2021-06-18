import datetime
import os
from enum import Enum

bot_token = os.environ.get("bot_token")

postgresql = os.environ.get("db_conn_str")

groups = [-1001459406039, -1001375138626]

token_for_refferral = 200000

texts = {
    'ru': {
        "hello": "Привет",
        "cabinet": "Кабинет🗒",
        "select_lang": "<b>Выберите язык</b>",
        "lang_name": "Русский🇷🇺",
        "participate_button": "Участвовать в Раздаче",
        "participate": """Привет Safe, я SafeBull AirDrop Bot
🤝
SafeBull – нечто большее чем
просто разрекламированная
монета.
В нашей команде много
разноплановых специалистов, но
Все мы заядлые
криптоэнтузиасты. Помимо
монеты SafeBull мы мыслим
масштабно и работаем над
собственными NFT токенами и
NFT биржей. В ближайшее время
Вся экосистема будет построена
на базе NFT SAFEBULL, что
соответственно еще сильнее
подтолкнет цену токена вверх и
увеличит количество холдеров.
Запуск нашего NFT совсем скоро,
не упусти момент!🥳
✅ Чтобы получить монеты в
раздаче тебе нужно выполнить
несколько заданий
⭐️За выполнение всех заданий –
Ты получишь 300.000 токенов
SAFEBULL
За приглашенного друга - Ты
получишь 200.000 токенов
SAFEBULL
Нажми "Участвовать в Раздаче"
чтобы продолжить""",
        "accept_rule": """📝Участвуя, ты соглашаешься на
условия и правила Раздачи SafeBull
<b>Пожалуйста, прочитай внимательно🙏</b>\n
❗️ Выполнив все задания ты получишь
максимальное количество токенов в
качестве вознаграждения, если ты не
выполнишь одно из условий - тогда
получить награду будет невозможно.\n
❗️ Все задания будут проверятся
командой модераторов и если будет
пропущено условие в Раздаче, токены
SafeBull не будут начислены. Мы хотим
чтобы вы получили максимальное
Количество токенов, поэтому
убедительно просим Вас выполнять все
задания и оставаться подписанными на
наши социальные сети до окончания
Раздачи. Если вы или ваш реферал
отпишется до окончания раздачи -
награда будет вычтена с вашего баланса!\n
Нажми <b>"Согласен"</b> если ты принимаешь
условия и правила Раздачи.""",
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
        "subscribe_groups": "Для того чтобы продолжить необходимо подписаться на все группы и каналы",
        "subscribe_check_false": "Необходимо подписатся на все каналы и группы",
        "set_bep_20": """Введи свой адрес кошелька BEP-20
(binance smart chain):
⚙️Адрес должен начинаться с 0х
⚙️Пример: 0xfa344c08c93066a4d6266063c6ebc63925a18467""",
        "invalid_bep_address": "Не корректный BEP 20 адресс\n⚙️<b>Пример</b>: 0xfa344c08c93066a4d6266063c6ebc63925a18467",
        'add_token_for_invite_user': 'Вам были начислены {} токен(a/ов) за приглощение юзера {}',
        "start_screen": "Спасибо Safe что участвовал в раздаче SafeBull.\nТвои детали:\n{}Вступил в Телеграмм канал/группу\n{}BEP-20 address: {}\nВаша реферальная ссылка: {}\nНа вашем счету: {} SAFEBULL",
        "owner_contacts_button": "📞Контакты",
        "owner_contacts": "Здесь должны быть контакты владельцев",
        "tokens_output_button": "💰Вывод",
        "tokens_output": "Напишите целое количество SAFEBULL которое вы хотите вывести.\n На вашем счету <b>{}</b> SAFEBULL.",
        "please_write_number": "🤦🏻<b>Введите число!</b>",
        "thnx_for_subscribes": "🎉Спасибо за подписку на наши ресурсы!",
        "output_order_created": "Заказ на вывод SafeBull был создан\n<b>Заказ №: {}</b>",
        "order_alr_exist": "⏱У вас уже есть заказ на вывод SafeBull, подождите пока ваш заказ одобрят, после чего вы сможете создать новый заказ",
        "cancel_button": "❌Отменить❌",
        "cancel": "✅Отменено✅",
        "not_enough_money": "🚧Не достаточно SafeBull на вашем счету"
    },
    'en': {
        "hello": "hello",
        "cabinet": "Сabinet🗒",
        "select_lang": "<b>Select you language</b>",
        "lang_name": "English🇺🇸",
        "participate": """Hi Safe, I'm SafeBull AirDrop Bot
🤝
SafeBull is more than
just advertised
coin.
There are many
diverse specialists, but
We are all avid
crypto enthusiasts. In addition to
SafeBull coins we think
large-scale and working on
own NFT tokens and
NFT exchange. In the near future
The whole ecosystem will be built
based on NFT SAFEBULL, which
correspondingly even stronger
will push the token price up and
will increase the number of holders.
The launch of our NFT is coming soon,
don't miss the moment!   
✅ To get coins in
the distribution you need to complete
several tasks
⭐️For completing all tasks -
You will receive 300,000 tokens
SAFEBULL
For an invited friend - You
you will receive 200,000 tokens
SAFEBULL
Click "Participate in the Giveaway"
to continue""",
        "participate_button": "Participate in the Giveaway",
        "accept_rule": """📝 By participating, you agree to
SafeBull Giveaway Terms and Conditions
<b>Please read carefully🙏</b>\n
❗️ After completing all the tasks you will receive
maximum number of tokens in
as a reward if you do not
you fulfill one of the conditions - then
it will be impossible to receive the reward.\n
❗️ All tasks will be checked
a team of moderators and if there is
missing condition in Hand, tokens
SafeBull will not be credited. We want
so that you get the maximum
The number of tokens, therefore
We kindly ask you to do all
assignments and stay subscribed to
our social networks until the end
Giveaways. If you or your referral
unsubscribe before the end of the distribution -
the reward will be deducted from your balance!\n
Click <b>"Agree"</b> if you accept
distribution terms and conditions.""",
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
        "subscribe_groups": "In order to continue, you need to subscribe to all groups and channels.",
        "subscribe_check_false": "You need to subscribe to all channels and groups",
        "set_bep_20": """Enter your BEP-20 wallet address
(binance smart chain):
⚙️Address must start with 0x
⚙️Example: 0xfa344c08c93066a4d6266063c6ebc63925a18467""",
        "invalid_bep_address": "Incorrect BEP 20 address\n⚙️<b>Example</b>: 0xfa344c08c93066a4d6266063c6ebc63925a18467",
        'add_token_for_invite_user': 'You were credited with {} token(s) for attracting a user {}',
        "start_screen": "Thank you Safe for contributing to the SafeBull distribution.\nYour details:\n{}Joined the Telegram channel/group.\n{} BEP-20 address: {}\nYour referral link: {} \nIn your account: {} SAFEBULL.",
        "owner_contacts_button": "📞Contacts",
        "owner_contacts": "There should be contacts of the owners here",
        "tokens_output_button": "💰Output",
        "tokens_output": "Write the whole amount of SAFEBULL you want to withdraw.\nYour account is <b>{}</b> SAFEBULL.",
        "please_write_number": "🤦🏻<b>Enter a number!</b>",
        "thnx_for_subscribes": "🎉Thank you for subscribing to our resources!",
        "output_order_created": "SafeBull withdrawal order has been created\n<b>Order №: {}</b>",
        "order_alr_exist": "⏱You already have a SafeBull withdrawal order, wait until your order is approved, after which you can create a new order",
        "cancel_button": "❌Cancel❌",
        "cancel": "✅Canceled✅",
        "not_enough_money": "🚧Not enough SafeBull in your account"
    }
}


group_leave_timeout_sec = 60*10


class Lang(Enum):
    ru = 1
    en = 2

Lang

DEFAULT_LANG = Lang.ru