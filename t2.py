import telebot
from telebot import types
import requests
import random
import json
import os

bot = telebot.TeleBot('8141636667:AAGzZZnmMQpV4CFMoQBeVWWfSop9FL2Pzzw')
API_TOKEN = "507677:AAM6JKp2eqkVSQcd14KlgGgBSEH7T8QqetF"
ADMIN_IDS = [7595424174]
SUPPORT_URL = "https://t.me/userdoxxsy"

WELCOME_PHOTO = "AgACAgEAAxkBAAMGaVJzuJuB-7s6NCvbdWAEsayQ1pAAAqcLaxvBvJBGPqZbFxfBpQIBAAMCAAN5AAM2BA"
MENU_PHOTO = "AgACAgEAAxkBAAMFaVJzuBgrPr-PrX8NlxpRAAGml2uSAAKmC2sbwbyQRnfOQNE8itRrAQADAgADeQADNgQ"
PROFILE_PHOTO = "AgACAgEAAxkBAAMHaVJzuB0HWXU2TLPrMe6YD-K8i8QAAqgLaxvBvJBGlDrkKpEjxFoBAAMCAAN5AAM2BA"
PAYMENT_BG = MENU_PHOTO

prices = {
    "Одежда": 2,
    "Раскрут": 2,
    "ИИ": 2,
    "Премиум схемы": 5,
    "Арбитраж": 2,
    "Интернет магазин": 2,
    "Белая товарка": 2,
    "Инста": 2.5,
    "Вк": 2.5,
    "Схемы": 3,
    "Сносер": 12,
    "Госки": 25,
    "Вериф фраги": 2,
    "Вериф кб": 10,
    "ТГ акки по лоу": 3,
    "Снятие сб": 0.5,
    "Яндекс сплит": 3,
    "Яндекс рефаунд": 3,
    "Тор прокси": 1
}

products = {
    "Одежда": "BQACAgIAAxkBAAMyaVKBDduWqEWXAR_sVoi_egFHm0cAAhdlAAKeEnFK8bY1QeBKBHA2BA",
    "Раскрут": "BQACAgIAAxkBAAMzaVKBDYIXvyehj4iHzNiYRWhGmA8AAkNlAAKeEnFK9eiQ_tLOt7E2BA",
    "ИИ": "BQACAgIAAxkBAAM0aVKBDbXsI68awoFWuvr9y-uFrLMAAj9lAAKeEnFKDnTjNlJBOPw2BA",
    "Премиум схемы": "BQACAgIAAxkBAAMmaVJ3PxQ2kwxDUfYwlkmfSd900s0AAqVHAAK6i8lIpPiPSz5kIdQ2BA",
    "Арбитраж": "BQACAgIAAxkBAAMsaVKAdRuGezIIORVmotmtySowu7oAAmBEAAJ5MqhIf_z75tDAjNE2BA",
    "Интернет магазин": "BQACAgIAAxkBAAMvaVKAtvVUpedJmUeBiCBCMhdUA_UAApAtAAJzWWlJGs1vQdN5qvA2BA",
    "Белая товарка": "BQACAgIAAxkBAAMuaVKAtoi5UoVDQYlOBrM0UTIILpQAAkVNAAKOEVFKnhwz1vsAAeIbNgQ",
    "Инста": "BQACAgIAAxkBAAM2aVKBDTh2Kwo2l0JNGSKpkuU6E_MAApc_AAJe-uBLVpDKLDt5UK42BA",
    "Вк": "BQACAgIAAxkBAAM1aVKBDS7o4ZbASHrJZZzGWVYsaQEAAoE_AAJe-uBL7GsMcHlP5Mc2BA",
    "Схемы": "BQACAgQAAxkBAAMqaVKAVHiLn3ALMCTlGBt-xpvd3LkAAiAPAALyLElS8VY5zAnG7RE2BA",
    "Сносер": "BQACAgEAAxkBAAMoaVJ3r-YnBvxp3CPZX0COsFzJKKwAAg8FAAJHpvhFM_8PwzSkhOQ2BA",
    "Госки": [
        "BQACAgUAAxkBAAMVaVJ2YPLK6_24Z5wVQscG2C68G18AAiwVAAI2wEFUtvHd7CCiGAM2BA",
        "BQACAgUAAxkBAAMZaVJ2YBuQ02rVvJ8pntwovkGl1_4AAi8VAAI2wEFUAAFrJvhQc0zENgQ",
        "BQACAgUAAxkBAAMaaVJ2YPA7rKizv5CiXbnXV-MNWjcAAjEVAAI2wEFUaESLpkK6x5M2BA"
    ],
    "Вериф фраги": [
        "AgACAgUAAxkBAAMkaVJ2_2vea2mgARNZgzsrsz-o2VYAAqjGMRs2wEFU5thvgWpps4sBAAMCAAN4AAM2BA",
        "BQACAgUAAxkBAAMWaVJ2YA_xRikeb882-GSAekNi3W4AAi0VAAI2wEFU9cftbd10G-o2BA",
        "BQACAgUAAxkBAAMXaVJ2YFpsCVbL8cT5H7mvwkgV6mUAAjAVAAI2wEFU6ccalDR8B4Q2BA",
        "BQACAgUAAxkBAAMYaVJ2YIDQMNcirAiZM8_9VmkhzOsAAi4VAAI2wEFU7HhV1wn9mjI2BA"
    ],
    "ТГ акки по лоу": """1.заходишь на сайт https://lzt.market 

2.регистрируешь аккаунт на сайте (это очень просто, войди через Гугл или другие сети).

3.пополняешь свой баланс, спускаемся вниз страницы и там будет кнопка пополнить баланс и пополняете баланс.

4.(ВАЖНО) после пополнения баланса заходим на главную и выбираем значок телеграм, дальше выставляем такие параметры:
До 30₽
Фишинг
Старые (по заливу).
Дальше нажимаем показать аккаунты.

5. Выбираем аккаунт который вам понравился и нажимаем купить.

6.(ВАЖНО) После покупки аккаунт мы нажимаем на "данные аккаунта" и там нам покажет номер аккаунта, вводим этот номер аккаунта в телеграм. Дальше мы заходим обратно на сайт и нажимаем на кнопку "получить код" и вводим данный код в телеграм.

7.(ВАЖНО) После того как вы зашли на аккаунт ничего не трогаем 24 часа (потому что аккаунт может слететь). После 24 часов вы можете пользоваться вашим аккаунтом.""",
    "Снятие сб": [
        "Здравствуйте!\nМой аккаунт был заблокирован за подозрение в нарушении правил Telegram. Хотел бы уточнить, что мои действия не нарушали правила Telegram. Возможно, я совершил ошибку, из-за которых мои действия были восприняты как спам. Однако, я никогда не использовал Telegram для рассылки нежелательных сообщений или вредоносной активности.",
        "Добрый день,я только создал аккаунт и хотел найти друга и поговорить с ним и мне бег моего ведома ограничили писать кому-либо,я не знаю из-за чего это могло произойти,но прошу вас снять ограничения.",
        "Мне неизвестно, почему на мой аккаунт были наложены ограничения. Я создал его для общения с друзьями, и никогда не использовал его для негативных действий, таких как рассылка спама или обман.",
        "Я не понимаю, почему были введены ограничения, так как я всегда уважительно отношусь к другим пользователям Telegram и никогда не отправляю ничего, что могло бы их расстроить. Пожалуйста, снимите эти ограничения.",
        "Здравствуйте!\nПрошу вас отменить спам-бан с моего аккаунта. Я живу в Украине, и, к сожалению, люди из России часто жалуются на меня. Я считаю, что это несправедливо по отношению ко мне.",
        "Понятия не имею. Аккаунт был взломан, только восстановил доступ. Использую исключительно для общения с коллегами по работе и родственниками.",
        "Дорогой Telegram! Вы очень важны для меня, и я ценю спокойствие других пользователей. Я не понимаю, почему мой аккаунт был заблокирован. Я просто хотел скачать Telegram, чтобы общаться с родственниками, а вы сообщаете, что это невозможно... Пожалуйста, разблокируйте меня, это для меня очень важно. Спасибо!",
        "Добрый день, я очень сильно сожалею о том, что получила бан и вовсе не хотела этого, я принимаю ошибку и не хочу этого бана, разблокируйте пожалуйста, если вы не можете этого сделать, то можете пожалуйста сказать через сколько меня выпустят с теневого бана? Состою я в нем уже огоколо полугода, хочу написать новым друзьям, чтобы знакомиться, но выскакивает этот же бан, надеюсь вы мне ответите на вопрос и поможете, спасибо.",
        "Здравствуйте! Я не понимаю по какой причине мне прилетел спам.Никому не спамил, не предлагал свои услуги и прочее, прошу снять ограничения, так как по работе необходимо общаться, спасибо!",
        "Здравствуйте, дорогая служба поддержка!\nЯ живу в Украине и не могу написать своим родственникам, так как мне установили спам-блок. Пожалуйста, снимите его, я не нарушал никаких правил.",
        "Здравствуйте, уважаемые сотрудники Telegram, я общался с друзьями, отправил в чат gif-изображение, и спам-система решила, что я нарушитель, и заблокировала меня.",
        "Здравствуйте!\nМой аккаунт был заблокирован за подозрение в нарушении правил Telegram. Хотел бы уточнить, что мои действия не нарушали правила Telegram. Возможно, я совершил ошибку, из-за которых мои действия были восприняты как спам. Однако, я никогда не использовал Telegram для рассылки нежелательных сообщений или вредоносной активности.\n\nЯ активно использовал Telegram для общения, работы и других целей. Кроме того, я отправлял средства в Telegram для поддержания платформы и считаю её незаменимым инструментом в своей повседневной жизни. Это делает мой аккаунт очень важным для меня. Прошу рассмотреть возможность пересмотра блокировки, так как я совершенно не согласен с вашим решением.\n\nЗаранее благодарю за ваше внимание и понимание! Если нужна дополнительная информация, готов её предоставить.",
        """Тема: Request to remove spam block

Текст:

Hello,

I am writing to request that the spam block be removed from my account.

Unfortunately, I have been the victim of malicious activity. Someone created a channel that was transferred to me, and then complaints were made about it. As a result, my account was blocked for spam, even though I had nothing to do with this channel until it was transferred to me.

I understand the importance of complying with the platform's rules and assure you that such situations will not occur in the future.

Please consider unblocking my account.

My contact details:

Telegram: t.me/ (ваш юзернейм)
ID: (ваш айди)
Thank you in advance for your help!"""
    ],
    "Яндекс сплит": """Яндекс сплит (разделение платежей)

Ссылки для изучения:
1. https://teletype.in/@keeperbett/GYR4u6hU_bM
2. https://teletype.in/@mraklaur/CC-7NtHv856""",
    "Яндекс рефаунд": """Рефаунд «Яндекс.Маркет»

1. Создаём аккаунт «Яндекс.Маркет»;
• Для крупных рефов используем гретые аккаунты, для всевозможной мелочи до 500₽ подойдут новореги;
2. Оформляем заказ с доставкой в постамат;
3. Как только заказ пришел, отправляемся в постамат и забираем его;
4. Возвращаемся домой и достаем содержимое посылки с помощью фена (при воздействии теплого воздуха клей нагреется и это позволит достать содержимое без повреждений упаковки). Меняем заказанный товар на всевозможный мусор и подгоняем его по весу. Немного мнём или надрываем коробку товара, после чего запаковываем его обратно в упаковку «Яндекс.Маркет» (важно, нужно мять и рвать именно коробку от товара, который вы заказывали, а не упаковку посылки), после чего делаем анпакинг на видео с нашими фейковыми пруфами;
• Видео с распаковкой необходимо только для крупных заказов, для мелочевки достаточно фотографий без всех этих заморочек;
5. Пишем в техподдержку нечто в духе: "Здравствуйте, забрал заказ из постамата, когда пришёл домой и открыл коробку офигел — вместо товара лежит какой-то мусор. Как мне вернуть деньги?";
6. Получаем возврат средств в течение нескольких дней.""",
    "Тор прокси": """Tor прокси (изменение IP)
Ссылки для изучения:
https://telegra.ph/Poluchaem-proksi-Tor-07-18"""
}

desc = {
    "Одежда": "Мануал по заработку на репликах популярных брендов",
    "Раскрут": "Подробный мануал по раскруту и пиару любых соц. сетей",
    "ИИ": "Мануал по заработку на ИИ контенте. 60$+ в день",
    "Премиум схемы": "100+ премиум схем для быстрого заработкая",
    "Арбитраж": "Курс по арбитражу крипты",
    "Интернет магазин": "Мануал как открыть свой первый интернет магазин и начать зарабатывать",
    "Белая товарка": "Подробное пособие для каждого, кто хочет войти в мир трафика, начиная с белых вертикалей",
    "Инста": "Мануал на раскрут и заработок с Инстаграм",
    "Вк": "Мануал по заработку с ВК",
    "Схемы": "100 схем для входа в разные ниши",
    "Сносер": "Сносер ТГ акков, ботов и каналов",
    "Госки": "БД со всеми нужными данными",
    "Вериф фраги": "Подробный мануал по верифу + паспорта",
    "ТГ акки по лоу": "Как ловить Telegram аккаунты с отлегой по низкой цене",
    "Снятие сб": "Текст для снятия спамблока в Telegram",
    "Яндекс сплит": "Яндекс сплит (разделение платежей) от А до Я",
    "Яндекс рефаунд": "Яндекс рефаунд от А до Я",
    "Тор прокси": "Краткий мануал по получению прокси для Tor браузера"
}

CARD = """
Банк: Тинькофф
Номер: 2200 7020 0053 8947
Получатель: Иван Иванов

После перевода отправьте скриншот чека.
Админ проверит и подтвердит оплату.
"""

pending_payments = {}
DATA_FILE = 'users_data.json'

def load_users_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_users_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def update_user_spent(user_id, amount):
    data = load_users_data()
    user_id_str = str(user_id)
    
    if 'users' not in data:
        data['users'] = {}
    
    if user_id_str not in data['users']:
        data['users'][user_id_str] = {
            'username': '',
            'total_spent': 0,
            'used_promocodes': [],
            'active_discount': 0
        }
    
    data['users'][user_id_str]['total_spent'] = data['users'][user_id_str].get('total_spent', 0) + amount
    save_users_data(data)

def get_user_spent(user_id):
    data = load_users_data()
    user_id_str = str(user_id)
    
    if 'users' in data and user_id_str in data['users']:
        return data['users'][user_id_str].get('total_spent', 0)
    return 0

def get_user_promocodes(user_id):
    data = load_users_data()
    user_id_str = str(user_id)
    
    if 'users' in data and user_id_str in data['users']:
        return data['users'][user_id_str].get('used_promocodes', [])
    return []

def get_user_discount(user_id):
    """Получает активную скидку пользователя (максимальную из использованных промокодов)"""
    data = load_users_data()
    user_id_str = str(user_id)
    
    if 'users' in data and user_id_str in data['users']:
        return data['users'][user_id_str].get('active_discount', 0)
    return 0

def add_used_promocode(user_id, promocode, discount):
    data = load_users_data()
    user_id_str = str(user_id)
    
    if 'users' not in data:
        data['users'] = {}
    
    if user_id_str not in data['users']:
        data['users'][user_id_str] = {
            'username': '',
            'total_spent': 0,
            'used_promocodes': [],
            'active_discount': 0
        }
    
    if promocode in data['users'][user_id_str].get('used_promocodes', []):
        return False
    
    if 'used_promocodes' not in data['users'][user_id_str]:
        data['users'][user_id_str]['used_promocodes'] = []
    
    data['users'][user_id_str]['used_promocodes'].append(promocode)
    
    current_discount = data['users'][user_id_str].get('active_discount', 0)
    if discount > current_discount:
        data['users'][user_id_str]['active_discount'] = discount
    
    if 'promocodes' not in data:
        data['promocodes'] = {}
    
    if promocode in data['promocodes']:
        if 'used_by' not in data['promocodes'][promocode]:
            data['promocodes'][promocode]['used_by'] = []
        
        if user_id not in data['promocodes'][promocode]['used_by']:
            data['promocodes'][promocode]['used_by'].append(user_id)
        
        if data['promocodes'][promocode].get('uses_left', float('inf')) > 0:
            uses_left = data['promocodes'][promocode].get('uses_left', float('inf'))
            if uses_left != float('inf'):
                data['promocodes'][promocode]['uses_left'] = uses_left - 1
    
    save_users_data(data)
    return True

def get_promocode_discount(promocode, user_id):
    data = load_users_data()
    promocode = promocode.upper()
    
    if 'promocodes' in data and promocode in data['promocodes']:
        promocode_data = data['promocodes'][promocode]
        
        user_id_str = str(user_id)
        if 'used_by' in promocode_data and user_id in promocode_data['used_by']:
            return -1
        
        uses_left = promocode_data.get('uses_left', float('inf'))
        if uses_left == 0:
            return -2
        
        return promocode_data.get('discount', 0)
    return -3

def get_pay_link(amount, product_name):
    headers = {"Crypto-Pay-API-Token": API_TOKEN}
    
    data = {
        "asset": "USDT",
        "amount": str(amount),
        "expires_in": 3600,
        "paid_btn_name": "openBot",
        "paid_btn_url": "https://t.me/sdfsdfsdfsfdsdfdsdfs_bot",
        "payload": product_name,
        "allow_comments": False,
        "allow_anonymous": True
    }
    
    try:
        response = requests.post(
            'https://pay.crypt.bot/api/createInvoice',
            headers=headers,
            json=data,
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            if result.get('ok'):
                invoice = result['result']
                return invoice['pay_url'], str(invoice['invoice_id'])
        
        return None, None
        
    except Exception as e:
        print(f"Ошибка запроса: {e}")
        return None, None

def check_invoice_status(invoice_id):
    headers = {"Crypto-Pay-API-Token": API_TOKEN}
    
    try:
        response = requests.get(
            f'https://pay.crypt.bot/api/getInvoices?invoice_ids={invoice_id}',
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            if result.get('ok') and result['result']['items']:
                invoice = result['result']['items'][0]
                return invoice['status']
        
        return None
        
    except Exception as e:
        print(f"Ошибка проверки счета: {e}")
        return None

@bot.message_handler(commands=['start'])
def start(message):
    show_welcome_screen(message.chat.id)

def show_welcome_screen(chat_id, message_id=None):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Меню", callback_data="menu"))
    markup.add(types.InlineKeyboardButton("Профиль", callback_data="profile"))
    markup.add(types.InlineKeyboardButton("Тех поддержка", url=SUPPORT_URL))
    
    if message_id:
        try:
            media = types.InputMediaPhoto(WELCOME_PHOTO, caption="Добро пожаловать!\nВыберите действие:")
            bot.edit_message_media(media=media, chat_id=chat_id, message_id=message_id)
            bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=markup)
        except:
            pass
    else:
        bot.send_photo(chat_id, WELCOME_PHOTO, caption="Добро пожаловать!\nВыберите действие:", reply_markup=markup)

@bot.message_handler(commands=['set_promo'])
def set_promo(message):
    if message.from_user.id not in ADMIN_IDS:
        return
    
    try:
        args = message.text.split()
        if len(args) < 3:
            bot.reply_to(message, "Формат: /set_promo CODE DISCOUNT% [USES]\nПример 1 (без лимита): /set_promo SUMMER20 20\nПример 2 (с лимитом): /set_promo SUMMER20 20 100")
            return
        
        promocode = args[1].upper()
        discount = int(args[2].replace('%', ''))
        
        data = load_users_data()
        
        if 'promocodes' not in data:
            data['promocodes'] = {}
        
        if len(args) == 4:
            uses = int(args[3])
            data['promocodes'][promocode] = {
                'discount': discount,
                'uses_left': uses,
                'used_by': []
            }
        else:
            data['promocodes'][promocode] = {
                'discount': discount,
                'uses_left': float('inf'),
                'used_by': []
            }
        
        save_users_data(data)
        
        if len(args) == 4:
            bot.reply_to(message, f"Промокод {promocode} установлен!\nСкидка: {discount}%\nДоступно активаций: {uses}")
        else:
            bot.reply_to(message, f"Промокод {promocode} установлен!\nСкидка: {discount}%\nАктиваций: безлимитно")
        
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")

@bot.message_handler(commands=['promos'])
def list_promocodes(message):
    if message.from_user.id not in ADMIN_IDS:
        return
    
    data = load_users_data()
    
    if 'promocodes' not in data or not data['promocodes']:
        bot.reply_to(message, "Нет активных промокодов")
        return
    
    promos_text = "Список промокодов:\n\n"
    
    for promocode, promo_data in data['promocodes'].items():
        discount = promo_data.get('discount', 0)
        used_count = len(promo_data.get('used_by', []))
        uses_left = promo_data.get('uses_left', 0)
        
        if uses_left == float('inf'):
            uses_left_str = "∞"
            total_str = f"{used_count}/{uses_left_str}"
        else:
            total_uses = used_count + uses_left
            total_str = f"{used_count}/{total_uses}"
        
        promos_text += f"• {promocode}[{total_str}] - {discount}%\n"
    
    bot.reply_to(message, promos_text)

@bot.callback_query_handler(func=lambda call: call.data == "menu")
def show_products_menu(call):
    markup = types.InlineKeyboardMarkup()
    
    for product_name in products.keys():
        price = prices.get(product_name, 0)
        button_text = f"{product_name} - {price}$"
        markup.add(types.InlineKeyboardButton(button_text, callback_data=f"buy_{product_name}"))
    
    markup.add(types.InlineKeyboardButton("Назад", callback_data="back_to_main"))

    try:
        media = types.InputMediaPhoto(MENU_PHOTO, caption="Выберите товар:")
        bot.edit_message_media(media=media, chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)
    except:
        pass

@bot.callback_query_handler(func=lambda call: call.data == "profile")
def show_profile(call):
    user_id = call.from_user.id
    spent = get_user_spent(user_id)
    used_promocodes = get_user_promocodes(user_id)
    active_discount = get_user_discount(user_id)
    
    profile_text = f"Ваш профиль:\n\n"
    profile_text += f"ID: {user_id}\n"
    profile_text += f"Всего потрачено: {spent}$\n"
    profile_text += f"Активная скидка: {active_discount}%\n"
    profile_text += f"Использовано промокодов: {len(used_promocodes)}\n\n"
    
    if active_discount == 0:
        profile_text += "Введите промокод для активации скидки:"
    else:
        profile_text += f"У вас уже есть скидка {active_discount}%\nНовые промокоды недоступны"
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Назад", callback_data="back_to_main"))

    try:
        media = types.InputMediaPhoto(PROFILE_PHOTO, caption=profile_text)
        bot.edit_message_media(media=media, chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)
    except:
        pass

@bot.message_handler(func=lambda message: True)
def handle_promocode(message):
    if message.text.startswith('/'):
        return
    
    user_id = message.from_user.id
    
    current_discount = get_user_discount(user_id)
    if current_discount > 0:
        bot.reply_to(message, f"У вас уже есть активная скидка {current_discount}%\nНовые промокоды недоступны")
        return
    
    promocode = message.text.upper()
    discount_result = get_promocode_discount(promocode, user_id)
    
    if discount_result == -1:
        bot.reply_to(message, "Вы уже активировали этот промокод")
    elif discount_result == -2:
        bot.reply_to(message, "Закончились активации этого промокода")
    elif discount_result == -3:
        bot.reply_to(message, "Неверный промокод")
    elif discount_result > 0:
        success = add_used_promocode(user_id, promocode, discount_result)
        if success:
            bot.reply_to(message, f"Промокод {promocode} активирован!\nСкидка: {discount_result}%")
        else:
            bot.reply_to(message, "Ошибка активации промокода")
    else:
        bot.reply_to(message, "Ошибка активации промокода")

@bot.callback_query_handler(func=lambda call: call.data == "back_to_main")
def back_to_main(call):
    show_welcome_screen(call.message.chat.id, call.message.message_id)

@bot.callback_query_handler(func=lambda call: call.data.startswith('buy_'))
def handle_buy(call):
    product_name = call.data.replace('buy_', '')
    base_price = prices.get(product_name, 0)
    
    user_discount = get_user_discount(call.from_user.id)
    
    if user_discount > 0:
        discounted_price = round(base_price * (1 - user_discount / 100), 2)
        price_text = f"{discounted_price}$ (скидка {user_discount}%)"
        final_price = discounted_price
    else:
        price_text = f"{base_price}$"
        final_price = base_price
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Оплатить CryptoBot", callback_data=f"pay_crypto_{product_name}"))
    markup.add(types.InlineKeyboardButton("Перевод на карту", callback_data=f"pay_card_{product_name}"))
    markup.add(types.InlineKeyboardButton("Назад", callback_data="menu"))
    
    caption = f"Товар: {product_name}\nЦена: {price_text}\nОписание:\n{desc.get(product_name)}\n\nВыберите способ оплаты:"
    
    try:
        media = types.InputMediaPhoto(MENU_PHOTO, caption=caption)
        bot.edit_message_media(media=media, chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)
    except:
        pass

@bot.callback_query_handler(func=lambda call: call.data.startswith('pay_crypto_'))
def handle_crypto_payment(call):
    product_name = call.data.replace('pay_crypto_', '')
    base_price = prices.get(product_name, 0)
    
    # ПРАВИЛЬНЫЙ расчет скидки
    user_discount = get_user_discount(call.from_user.id)
    if user_discount > 0:
        # Округление как в handle_buy()
        final_price = round(base_price * (1 - user_discount / 100), 2)
        if final_price < 0.02:  # Минимальная цена
            final_price = 0.02
    else:
        final_price = base_price
    
    # ВАЖНО: передаем final_price, а не base_price!
    pay_url, invoice_id = get_pay_link(final_price, product_name)
    
    if pay_url and invoice_id:
        pending_payments[invoice_id] = {
            'product': product_name,
            'user_id': call.from_user.id,
            'chat_id': call.message.chat.id,
            'message_id': call.message.message_id,
            'price': final_price  # Сохраняем финальную цену со скидкой
        }
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Оплатить", url=pay_url))
        markup.add(types.InlineKeyboardButton("Проверить оплату", callback_data=f"check_{invoice_id}"))
        markup.add(types.InlineKeyboardButton("Отмена", callback_data=f"buy_{product_name}"))
        
        # В сообщении показываем правильную цену
        if user_discount > 0:
            caption = f"Товар: {product_name}\nСумма: {final_price} USDT (скидка {user_discount}%)\n\n1. Нажмите 'Оплатить'\n2. Оплатите счет в @CryptoBot\n3. Вернитесь и нажмите 'Проверить оплату'"
        else:
            caption = f"Товар: {product_name}\nСумма: {final_price} USDT\n\n1. Нажмите 'Оплатить'\n2. Оплатите счет в @CryptoBot\n3. Вернитесь и нажмите 'Проверить оплату'"
        
        try:
            media = types.InputMediaPhoto(PAYMENT_BG, caption=caption)
            bot.edit_message_media(media=media, chat_id=call.message.chat.id, message_id=call.message.message_id)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)
        except:
            pass
    else:
        # Если не удалось создать счет
        try:
            bot.answer_callback_query(call.id, "Ошибка создания счета. Попробуйте позже.", show_alert=True)
        except:
            pass

@bot.callback_query_handler(func=lambda call: call.data.startswith('check_'))
def check_payment(call):
    invoice_id = call.data.replace('check_', '')
    
    if invoice_id in pending_payments:
        status = check_invoice_status(invoice_id)
        
        if status == 'paid':
            payment_info = pending_payments[invoice_id]
            send_product(payment_info)
            
            update_user_spent(payment_info['user_id'], payment_info['price'])
            
            del pending_payments[invoice_id]
            
            try:
                media = types.InputMediaPhoto(WELCOME_PHOTO, caption="Оплата подтверждена!\nТовар отправлен.")
                bot.edit_message_media(media=media, chat_id=call.message.chat.id, message_id=call.message.message_id)
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
            except:
                pass
        elif status == 'expired':
            del pending_payments[invoice_id]
            product_name = pending_payments.get(invoice_id, {}).get('product')
            if product_name:
                base_price = prices.get(product_name, 0)
                user_discount = get_user_discount(call.from_user.id)
                
                if user_discount > 0:
                    discounted_price = round(base_price * (1 - user_discount / 100), 2)
                    price_text = f"{discounted_price}$ (скидка {user_discount}%)"
                else:
                    price_text = f"{base_price}$"
                
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton("Оплатить CryptoBot", callback_data=f"pay_crypto_{product_name}"))
                markup.add(types.InlineKeyboardButton("Перевод на карту", callback_data=f"pay_card_{product_name}"))
                markup.add(types.InlineKeyboardButton("Назад", callback_data="menu"))
                
                caption = f"Товар: {product_name}\nЦена: {price_text}\nОписание:\n{desc.get(product_name)}\n\nСчет просрочен. Выберите способ оплаты:"
                
                try:
                    media = types.InputMediaPhoto(MENU_PHOTO, caption=caption)
                    bot.edit_message_media(media=media, chat_id=call.message.chat.id, message_id=call.message.message_id)
                    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=markup)
                except:
                    pass

@bot.callback_query_handler(func=lambda call: call.data.startswith('pay_card_'))
def handle_card_payment(call):
    product_name = call.data.replace('pay_card_', '')
    base_price = prices.get(product_name, 0)

    # ТАКОЙ ЖЕ расчет скидки
    user_discount = get_user_discount(call.from_user.id)
    if user_discount > 0:
        final_price = round(base_price * (1 - user_discount / 100), 2)
        if final_price < 0.01:
            final_price = 0.01
    else:
        final_price = base_price
    
    user_id = call.from_user.id
    pending_payments[user_id] = {
        'product': product_name,
        'price': final_price,  # Финальная цена со скидкой
        'type': 'card',
        'chat_id': call.message.chat.id,
        'message_id': call.message.message_id
    }
    
    # В сообщении показываем правильную цену
    if user_discount > 0:
        caption = f"Товар: {product_name}\nСумма: {final_price} USDT (скидка {user_discount}%)\n\n{CARD}\nОтправьте скриншот чека:"
    else:
        caption = f"Товар: {product_name}\nСумма: {final_price} USDT\n\n{CARD}\nОтправьте скриншот чека:"
    
    try:
        media = types.InputMediaPhoto(PAYMENT_BG, caption=caption)
        bot.edit_message_media(media=media, chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    except:
        pass

@bot.message_handler(content_types=['photo'])
def handle_screenshot(message):
    user_id = message.from_user.id
    
    if user_id in pending_payments and pending_payments[user_id]['type'] == 'card':
        payment_info = pending_payments[user_id]
        product_name = payment_info['product']
        price = payment_info['price']
        
        for admin_id in ADMIN_IDS:
            try:
                bot.send_message(
                    admin_id,
                    f"Новая заявка на оплату картой\n"
                    f"Пользователь: @{message.from_user.username or 'нет'} (ID: {user_id})\n"
                    f"Товар: {product_name}\n"
                    f"Сумма: {price} USDT"
                )
                bot.forward_message(admin_id, message.chat.id, message.message_id)
                
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton("Подтвердить", callback_data=f"approve_{user_id}"))
                markup.add(types.InlineKeyboardButton("Отклонить", callback_data=f"reject_{user_id}"))
                bot.send_message(admin_id, "Проверьте скриншот:", reply_markup=markup)
            except:
                pass
        
        bot.reply_to(message, "Скриншот отправлен на проверку. Ожидайте подтверждения админа.")
    else:
        bot.reply_to(message, "Вы не отправляли заявку на оплату картой.")

@bot.callback_query_handler(func=lambda call: call.data.startswith(('approve_', 'reject_')))
def handle_admin_decision(call):
    if call.from_user.id not in ADMIN_IDS:
        return
    
    action, user_id = call.data.split('_')
    user_id = int(user_id)
    
    if user_id in pending_payments:
        if action == 'approve':
            send_product(pending_payments[user_id])
            update_user_spent(user_id, pending_payments[user_id]['price'])
            bot.send_message(user_id, "Оплата подтверждена! Товар отправлен.")
        else:
            bot.send_message(user_id, "Оплата отклонена администратором.")
        
        del pending_payments[user_id]
        bot.delete_message(call.message.chat.id, call.message.message_id)

def send_product(payment_info):
    product_name = payment_info['product']
    chat_id = payment_info['chat_id']
    
    if product_name in products:
        product_data = products[product_name]
        
        if isinstance(product_data, list) and product_data:
            if product_name == "Снятие сб":
                text_to_send = random.choice(product_data)
                try:
                    bot.send_message(chat_id, text_to_send)
                except:
                    pass
            else:
                for item in product_data:
                    try:
                        if item.startswith(('BQACAg', 'AgACAg')):
                            bot.send_document(chat_id, item)
                        else:
                            bot.send_message(chat_id, item)
                    except:
                        pass
        elif isinstance(product_data, str) and product_data:
            if product_data.startswith(('BQACAg', 'AgACAg')):
                try:
                    bot.send_document(chat_id, product_data)
                except:
                    pass
            else:
                try:
                    bot.send_message(chat_id, product_data)
                except:
                    pass

print("Бот запущен...")
bot.infinity_polling()
