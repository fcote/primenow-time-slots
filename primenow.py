from datetime import datetime

import config
from telegram import Telegram, TelegramMessage
from primenow_api import PrimeNowAPI


class PrimeNow:
    merchant = None
    n_errors = 0
    products = []

    def __init__(self, merchant):
        self.merchant = merchant

    def check(self):
        primenow_api = PrimeNowAPI(self.merchant)

        print(f'Checking {self.merchant.get("name")}...')

        try:
            available_windows = primenow_api.get_available_windows()
        except RuntimeError:
            self.n_errors += 1

            self.save_response_logs(primenow_api.response, 'response_error.html')

            if self.n_errors == 3:
                self.notify(TelegramMessage.error_message())

                raise Exception('Error on check windows')

            return

        self.check_products(primenow_api)

        if len(available_windows) > 0:
            self.notify(TelegramMessage.found_message(self.merchant, available_windows))

            self.save_response_logs(primenow_api.response, 'response_ranges.html')

            return True
        else:
            self.reset_errors()

            print(f'No available windows on {self.merchant.get("name")} at {datetime.now().strftime("%H:%M:%S")}')

        return False

    def check_products(self, primenow_api):
        cart_items = primenow_api.get_products()

        products_removed = []
        products_quantity_decreased = []

        for product in self.products:
            item = next((item for item in cart_items if item['product'] == product['product']), None)

            if item is None:
                products_removed.append(product)
            elif item['quantity'] < product['quantity']:
                products_quantity_decreased.append(item)

        alerts = ''

        if len(products_removed) > 0:
            alerts += TelegramMessage.products_unavailable_message(self.merchant, products_removed)

        if len(products_quantity_decreased) > 0:
            alerts += TelegramMessage.products_quantity_decreased_message(self.merchant, products_quantity_decreased)

        if alerts != '':
            self.notify(alerts)

        self.products = cart_items

    def reset_errors(self):
        self.n_errors = 0

    @staticmethod
    def notify(message):
        print(f'Sending telegram message: {message}')

        if config.telegram_active:
            Telegram.send_message(message)

    @staticmethod
    def save_response_logs(response, filename):
        with open(config.get_path(f'logs/{filename}'), 'w') as file:
            file.write(response.text)
