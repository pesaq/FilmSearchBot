from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command
from database import DBManeger
from core.keyboards.commands import set_commands
from core.keyboards.help_keyboard import help_keyboard
from core.settings import get_settings

basicrouter = Router()
db_maneger = DBManeger('movies.db')
settings = get_settings('.env')

@basicrouter.startup()
async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Bot started')
@basicrouter.shutdown()
async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Bot stoped')

@basicrouter.message(Command(commands=['start']))
async def get_start(message: Message, bot: Bot):
    await set_commands(bot)
    await message.answer('Привет! Я бот для поиска фильмов по коду.\nЖми кнопку ниже для поиска!', reply_markup=help_keyboard)
