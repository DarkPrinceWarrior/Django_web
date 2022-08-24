from django.core.management.base import BaseCommand
from aiogram import types
from aiogram import Dispatcher, Bot, executor

bot = Bot(token="5442595961:AAFW_4y8vesQaPMQZXhrKruPNVXIPTHoauc")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start_message(message: types.Message):
    await message.answer('hello there!')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
