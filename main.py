import time

import config
from primenow import PrimeNow

if __name__ == '__main__':
    merchant_to_check = config.merchant_to_check
    merchant_checker = PrimeNow({
        "name": merchant_to_check,
        "id": config.primenow_merchants[merchant_to_check]
    })
    stop = False

    while not stop:
        if merchant_checker.check() and config.stops_if_found:
            stop = True

        time.sleep(config.checks_interval)
