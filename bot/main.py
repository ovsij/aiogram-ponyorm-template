from aiogram.utils import executor
import logging

from loader import dp

import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, skip_updates=True)