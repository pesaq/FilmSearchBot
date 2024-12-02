from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot: Bot):
    commands_lst = [
        BotCommand(
            command='start',
            description='Начало работы'
        )
    ]
    await bot.set_my_commands(commands_lst, BotCommandScopeDefault())