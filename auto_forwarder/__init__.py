import logging
import os
import sys

import telegram.ext as tg

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)

    from auto_forwarder.config import Development as Config
    API_KEY = Config.API_KEY
    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

    try:
        FROM_CHATS = set(int(x) for x in Config.FROM_CHATS)
    except ValueError:
        raise Exception("Your FROM_CHATS list does not contain valid integers.")

    try:
        TO_CHATS = set(int(x) for x in Config.TO_CHATS or [])
    except ValueError:
        raise Exception("Your TO_CHATS list does not contain valid integers.")

    WEBHOOK = Config.WEBHOOK
    IP_ADDRESS = Config.IP_ADDRESS
    URL = Config.URL
    PORT = Config.PORT
    CERT_PATH = Config.CERT_PATH

    WORKERS = Config.WORKERS


updater = tg.Updater(API_KEY, workers=WORKERS)

dispatcher = updater.dispatcher

FROM_CHATS = list(FROM_CHATS)
TO_CHATS = list(TO_CHATS)
