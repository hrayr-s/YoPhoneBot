import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


class Config(object):
    DEBUG = True
    BASE_API_URL = 'https://yoai.yophone.com/api/pub'
    CHECK_UPDATE_INTERVAL_SECONDS = 5
    BOT_TOKEN = os.environ.get('YOPHONE_BOT_TOKEN')
