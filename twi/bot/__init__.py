from aiogram import Dispatcher, Bot, executor

bot = Bot(token="5442595961:AAFW_4y8vesQaPMQZXhrKruPNVXIPTHoauc")
dp = Dispatcher(bot)
executor.start_polling(dp, skip_updates=True)
