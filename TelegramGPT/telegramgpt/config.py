import os
import sys

from loguru import logger
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = str(os.getenv("OPENAI_API_KEY"))
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID"))


LOG_LEVEL = str(os.getenv("LOG_LEVEL", "INFO"))
logger.remove()
logger.add(sys.stderr, level=LOG_LEVEL)
