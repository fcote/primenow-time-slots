# 📦 Amazon Prime Now time slots checker

## Setup

### Install the dependencies
```.bash
pip install -r requirements.txt
```

### Fill out the `.env` file
```.bash
cp .env.example .env
```

See the "Environments variables" section to fill it

### Fill out the `primenow_merchants.json` file

Each key should match a primenow merchant name.

Each value should match the id of the given primenow merchant.

You can retrieve the id of the merchant by going to any merchant on the primenow website and looking for the `merchantId` query params in your browser url bar.

Example:
For `https://primenow.amazon.fr/storefront?merchantId=AGMEOZFASZJSS` The id is `AGMEOZFASZJSS`


`primenow_merchants.json` example:
```.json
{
    "Monoprix": "A39IAEDNN88TCS",
    "Amazon": "AGMEOZFASZJSS"
}
```

## Environments variables
**CHECKS_INTERVAL**

Interval in seconds between each time slot check

**STOPS_IF_FOUND**

Whether or not to stop if an available time slot has been found

**MERCHANT_TO_CHECK**

The target merchant to check (Should match one of the entry in the primenow_merchants.json file)

**TELEGRAM_BOT_ACTIVE**

Whether or not you want to be notified on Telegram

**TELEGRAM_BOT_TOKEN**

The telegram bot token (See the "Telegram setup" section) <br>
Only required the if `TELEGRAM_BOT_ACTIVE` is set to `true`

**TELEGRAM_CHAT_ID**

Your telegram chat id (See the "Telegram setup" section) <br>
Only required the if `TELEGRAM_BOT_ACTIVE` is set to `true`

**COOKIE_UBID_ACBFR** / 
**COOKIE_X_ACBFR** / 
**COOKIE_AT_ACBFR** /
**COOKIE_SESS_AT_ACBFR**

:warning: Required, the script will bot work is these variable are not filled. <br>

These are the primenow cookies, used to make the requests <br>
You can find these by pressing F12 on Prime Now checkout page (Application->Cookies)

#### Default values
```.env
CHECKS_INTERVAL=60
STOPS_IF_FOUND=true
MERCHANT_TO_CHECK=Amazon

TELEGRAM_BOT_ACTIVE=false
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=

COOKIE_UBID_ACBFR=
COOKIE_X_ACBFR=
COOKIE_AT_ACBFR=
COOKIE_SESS_AT_ACBFR=
```

## Telegram setup

- Send `/start` to `@BotFather` on Telegram
- Give a name to your bot
- Copy the token given in the response (Store it safely!). This is the `TELEGRAM_BOT_TOKEN` env var
- Send a message to your bot (anything)
- Go to `https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates`, replace `{TELEGRAM_BOT_TOKEN}` by your token value
- Look for the `chat` key and copy the `id` value. This is the `TELEGRAM_CHAT_ID`

You're all set congrats !



