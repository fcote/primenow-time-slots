import requests

import config


class Telegram:
    TELEGRAM_URL = 'https://api.telegram.org'

    @staticmethod
    def send_message(message):
        return requests.get('{telegram_url}/bot{token}/sendMessage?chat_id={chat_id}&text={message}'.format(
            telegram_url=Telegram.TELEGRAM_URL,
            token=config.telegram_token,
            chat_id=config.telegram_chat_id,
            message=message
        ))


class TelegramMessage:
    @staticmethod
    def found_message(merchant, available_windows):
        return f'Des créneaux sont disponibles chez {merchant.get("name")}!\n\n' + '\n'.join(available_windows)

    @staticmethod
    def products_unavailable_message(merchant, products_removed):
        message = f'Ces produits ne sont plus disponibles et ont été supprimés de votre panier ({merchant.get("name")}):\n\n'
        message += '\n'.join(['- ' + product['product'] for product in products_removed]) + '\n\n'
        return message

    @staticmethod
    def products_quantity_decreased_message(merchant, products_quantity_decreased):
        message = f'Ces produits ont baissés en quantité dans votre panier ({merchant.get("name")}):\n\n'
        message += '\n'.join(['- ' + product['product'] + f" ({product['quantity']})" for product in products_quantity_decreased]) + '\n\n'
        return message

    @staticmethod
    def error_message():
        return 'Une erreur est survenue'