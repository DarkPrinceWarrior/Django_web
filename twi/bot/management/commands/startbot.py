from django.core.management.base import BaseCommand
from aiogram import types

from twi.bot import dp


@dp.message_handler(commands=['start', 'help'])
async def start_message(message: types.Message):
    await message.answer('hello there!')

# class Command(BaseCommand):
#     help = "Start bot"
#
#     def add_arguments(self, parser):
#         parser.add_argument("bot_id", nargs='?', type=int)
#         parser.add_argument('--port', help="Set Bot Runner Port (default: 5555)", default=5555, type=int)
#
#     def handle(self, *args, **options):
#         if options['bot_id'] is None:
#             self.stdout.write("Error. Bot id is required!")
#             return
#         self.stdout.write("Sending command....")
#         resp = start_bot(options['bot_id'], options['port'])
#         print(resp)
