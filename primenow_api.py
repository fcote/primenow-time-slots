import requests
import re
from bs4 import BeautifulSoup

import config


class PrimeNowAPI:
    ENDPOINT = 'https://primenow.amazon.fr/checkout/enter-checkout?merchantId='

    response = None

    def __init__(self, merchant):
        self.merchant = merchant

    def request(self):
        self.response = requests.get(
            url=self.ENDPOINT + self.merchant['id'],
            headers=self.headers(),
            cookies=config.cookie)

    def get_available_windows(self):
        if not self.response:
            self.request()

        html_response = BeautifulSoup(self.response.text, 'html.parser')

        if len(html_response.select('form#delivery-slot-form')) != 1:
            raise RuntimeError('This is not the checkout page.')

        available_windows = html_response.select('[data-a-input-name="delivery-window-radio"] span.a-color-base')

        return [window.text.replace('\n', '').strip() for window in available_windows]

    def get_products(self):
        if not self.response:
            self.request()

        html_response = BeautifulSoup(self.response.text, 'html.parser')

        return [{
            'product': item.select('.a-text-bold')[0].text.replace('\n', '').strip(),
            'quantity': re.match(".*?Qté.: ([0-9]*)", item.text.replace('\n', '')).groups()[0]
        } for item in html_response.select('.checkout-item-container')]

    @staticmethod
    def headers():
        user_agent = 'Mozilla/5.0 (X11;Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'

        return {
            'User-Agent': user_agent,
        }
