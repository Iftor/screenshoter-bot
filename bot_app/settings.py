import os

from dotenv import load_dotenv

from bot_app import screenshots

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

BOT_TOKEN = os.environ.get('BOT_TOKEN', '')

SPLASH_PORT = os.environ.get('SPLASH_PORT', '8050')

SAVE_PATH = screenshots.get_dir_path()

FULL_PAGE = 1
