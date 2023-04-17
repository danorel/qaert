import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# environment settings
IS_PRODUCTION = os.environ.get("ENVIRONMENT", "development") == "production"

# bot settings
TOKEN = str(os.environ.get("TOKEN"))
