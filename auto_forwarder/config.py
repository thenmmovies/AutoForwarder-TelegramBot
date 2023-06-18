

# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "6043062672:AAH76W9fh5Iw6KSN8epvG_2GETas94EAeZI"  # Your bot API key
    OWNER_ID = "1224313313" # Your user id

    # Make sure to include the '-' sign in group and channel ids.
     FROM_CHATS = [-1001862773794]  # List of chat id's to forward messages from
    TO_CHATS = [-1001982159948]  # List of chat id's to forward messages to
     
    # FOR WEBHOOKS
    WEBHOOK = False
    IP_ADDRESS = "127.0.0.1"  # Use "0.0.0.0" if using Heroku
    URL = None  # The URL that the bot should listen to for updates
    PORT = 5000  # Port to listen on for webhooks
    CERT_PATH = None  # Path to certificate file

    WORKERS = 4  # Depends on usage, 4 by default
    REMOVE_TAG = False

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
