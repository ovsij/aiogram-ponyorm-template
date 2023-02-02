from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import bot, dp
from bot.keyboards.callback import inline_kb_start

from database.crud import *
from database.models import *

@dp.message_handler(CommandStart)
async def bot_start(message: types.Message):
    register_user(message.from_user)
    text, reply_markup = inline_kb_start(message.from_user)

    await bot.send_message(
        message.from_user.id,
        text=text,
        reply_markup=reply_markup
    )