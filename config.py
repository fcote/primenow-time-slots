import dotenv
import json
from os import getenv
from os.path import dirname, abspath

dotenv.load_dotenv()


def get_path(filename):
    return f'{dirname(abspath(__file__))}/{filename}'


telegram_enabled = getenv('TELEGRAM_BOT_ENABLED', 'false') == 'true'
telegram_token = getenv('TELEGRAM_BOT_TOKEN')
telegram_chat_id = getenv('TELEGRAM_CHAT_ID')

cookie = {
    'ubid-acbfr': getenv('COOKIE_UBID_ACBFR'),
    'x-acbfr': getenv('COOKIE_X_ACBFR'),
    'at-acbfr': getenv('COOKIE_AT_ACBFR'),
    'sess-at-acbfr': getenv('COOKIE_SESS_AT_ACBFR'),
}

checks_interval = int(getenv("CHECKS_INTERVAL", '60'))
stops_if_found = getenv("STOPS_IF_FOUND", 'true') == 'true'

merchant_to_check = getenv("MERCHANT_TO_CHECK", "Amazon")

with open(get_path('primenow_merchants.json'), 'r') as file:
    primenow_merchants = json.load(file)
