from aiogram import types

from loader import dp

from database.crud import *
from database.models import *

# обработчик кнопок
@dp.callback_query_handler(lambda c: c.data.startswith('btn'))
async def btn_callback(callback_query: types.CallbackQuery):
    code = callback_query.data
    print(code)