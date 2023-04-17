import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# environment settings
IS_PRODUCTION = os.environ.get("ENVIRONMENT", "development") == "production"

# bot settings
TOKEN = str(os.environ.get("TOKEN"))

# heroku settings
HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8443)
