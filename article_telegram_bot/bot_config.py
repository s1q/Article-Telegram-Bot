"""
Это конфигурационный файл для Article Telegram Bot.
Заполните поля ниже перед тем, как запускать бота через main.py!
"""

import re

from .tools import get_env_var


# "bot_token" - Токен для бота. Можно получить в Telegram, создав бота в @BotFather
bot_token = get_env_var('TELEGRAM_BOT_TOKEN', required=True)


# "user_secret" - пароль для добавления текущего пользователя в список получателей.
# Отправьте его боту, чтобы добавить текущего пользователя.
# Поставьте значение None, чтобы выключить защиту и включить команду /subscribe
user_secret = get_env_var('SUBSCRIBE_SECRET')


# "database_uri" - ссылка на базу данных Heroku Postgres.
database_url = get_env_var('DATABASE_URL', required=True)

# "key_words" - ключевые слова.
regular_key_words = get_env_var('REGULAR_KEYWORDS', default='.*')
parsers = {
    'РИА Новости': {
        'key_words': re.compile(regular_key_words),
        'send_key_words': True,
        'use': True
    },
    'Reuters.com': {
        'key_words': re.compile(re.compile(regular_key_words)),
        'send_key_words': True,
        'use': True
    },
    'Ru EuroNews': {
        'key_words': re.compile(regular_key_words),
        'send_key_words': True,
        'use': True
    },
    'TourProm.ru': {
        'key_words': re.compile(regular_key_words),
        'send_key_words': True,
        'use': True
    },
    'Lenta.Ru': {
        'key_words': re.compile(regular_key_words),
        'send_key_words': True,
        'use': True
    },
    'InoSmi': {
        'key_words': re.compile(regular_key_words),
        'send_key_words': True,
        'use': True
    },
    'BBC News': {
        'key_words': re.compile(regular_key_words),
        'send_key_words': True,
        'use': True
    },
    'IranToday': {
        'key_words': re.compile('.*'),
        'send_key_words': False,
        'use': True
    },
    'Arabian Business News': {
        'key_words': re.compile('.*'),
        'send_key_words': False,
        'use': False
    },
    'Sana News EN': {
        'key_words': re.compile('.*'),
        'send_key_words': False,
        'use': True
    },
    'Sana News RU': {
        'key_words': re.compile('.*'),
        'send_key_words': False,
        'use': True
    },
    'NNA News': {
        'key_words': re.compile('.*'),
        'send_key_words': False,
        'use': False
    },
    'Y-Oman News': {
        'key_words': re.compile('.*'),
        'send_key_words': False,
        'use': False
    },
    'YeniSafak News': {
        'key_words': re.compile('.*'),
        'send_key_words': False,
        'use': True
    },
    'EgyptianStreets News': {
        'key_words': re.compile('.*'),
        'send_key_words': False,
        'use': True
    },
    'QatarLiving News': {
        'key_words': re.compile('.*'),
        'send_key_words': False,
        'use': True
    },
    'MehrNews': {
        'key_words': re.compile('.*'),
        'send_key_words': False,
        'use': True
    },
    'ArabNews': {
        'key_words': re.compile('.*'),
        'send_key_words': False,
        'use': True
    },
    'EgyptToday News': {
        'key_words': re.compile('.*'),
        'send_key_words': False,
        'use': True
    },
}

# "main_language" - язык, на который будет переведён текст статьи.
# "translate" - переводить ли статьи на язык "main_language". True или False.
# Для перевода требуется API Ключ Yandex. Его можно получить на странице https://translate.yandex.com/developers/keys
yandex_api_key = get_env_var('YANDEX_TRANSLATE_API_KEY', default='EMPTY')
main_language = str(get_env_var('ATB_DEFAULT_LANGUAGE', default='ru'))
translate = bool(get_env_var('ATB_DO_TRANSLATE', default=False))

# "parse_interval" - переодичность, с которой бот проверяет сайты (в секундах). Рекомендуется указать от 30 секунд.
parse_interval = int(get_env_var('ATB_PARSE_INTERVAL', default=30))

# "use_proxy" - использовать ли прокси для обхода блокировки Telegram в РФ (имеет только 2 значения: True - да, или False - нет).
# Рекомендуется использовать Tor Bundle proxy как бесплатный, стабильный и наиболее безопасный вариант.
# "proxies" преднастроена для использования Tor Bundle proxy.
# Heroku не требует прокси (пока что), поэтому при деплое на Heroku ставим False, иначе бот не запустится.
use_proxy = get_env_var('USE_PROXY', default=False)
proxies = {
    'https': get_env_var('ATB_PROXY', default='socks5://127.0.0.1:9050')
}

logging_format = get_env_var('LOGGING_FORMAT', default='{time} [{level}] {message}')
logging_level = get_env_var('LOGGING_LEVEL', default='INFO')