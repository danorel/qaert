import logging

from aiogram import Bot, executor, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from constants import *
from middlewares import *
from qa import *

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
dp.middleware.setup(ThrottlingMiddleware())


users = {}


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm Quaert!\nIntroduce yourself!")


@dp.message_handler()
@rate_limit(5, 'answer')
async def answer(message: types.Message):
    introduction = users.get(message.chat.id)
    if not introduction:
        users[message.chat.id] = message.text
        answer = "Thanks for you personal story.\nI am ready to answer your questions!"
    else:
        question = message.text
        answer = answer_question(question, introduction)
    await message.answer(answer)


async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()


def run():
    if IS_PRODUCTION:
        start_webhook(
            dispatcher=dp,
            webhook_path=WEBHOOK_PATH,
            skip_updates=True,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            host=WEBAPP_HOST,
            port=WEBAPP_PORT,
        )
    else:
        executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    run()
