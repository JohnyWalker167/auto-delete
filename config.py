import os
from dotenv import load_dotenv
import logging
from logging.handlers import RotatingFileHandler
from os import environ
from requests import get as rget

LOG_FILE_NAME = "log.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

logger = logging.getLogger(__name__)


load_dotenv('config.env', override=True)

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')
OWNER_USERNAME = os.getenv('OWNER_USERNAME')
OWNER_ID = int(os.getenv('OWNER_ID'))
STRING_SESSION = os.getenv('STRING_SESSION')


