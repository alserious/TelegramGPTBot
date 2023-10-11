import inspect
import sys

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


# from telegramgpt.gpt import send_message_to_openai
from telegramgpt.config import BOT_TOKEN, ADMIN_CHAT_ID, logger


bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=["help"], chat_id=ADMIN_CHAT_ID)
async def cmd_help(message: types.Message):
    """Return all available command."""

    logger.debug(f"Got message: {message}")

    command_list = [
        name.replace("cmd_", "/")
        for name, obj in inspect.getmembers(sys.modules[__name__])
        if (inspect.isfunction(obj) and name.startswith("cmd_"))
    ]
    commands = "\n".join(command_list)

    await message.reply(f"Active commands:\n{commands}")


@dp.message_handler(commands=["check"], chat_id=ADMIN_CHAT_ID)
async def cmd_check(message: types.Message):
    """Check bot status."""

    logger.debug(f"Got message: {message}")
    logger.info("Check")

    await message.reply("OK!")


@dp.message_handler(commands=["send_to_openai"], chat_id=ADMIN_CHAT_ID)
async def cmd_send_to_openai(message: types.Message):
    """Send message to openai."""

    logger.debug(f"Got message: {message}")

    # result = await send_message_to_openai(message=message)
    # if result:
    #     await message.reply(result)
    # else:
    #     logger.error(f"Do not get result for message: {message}")
    #     await message.reply("Internal error")


def start_bot() -> None:
    executor.start_polling(dispatcher=dp, skip_updates=True)
