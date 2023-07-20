from typing import Dict, List, Tuple, Union

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class InlineConstructor:

    @staticmethod
    def create_kb(
        text_and_data: list,
        schema: list = None
    ) -> InlineKeyboardMarkup:
        kb = InlineKeyboardMarkup()
        schema = [1 for i in range(len(text_and_data))] if not schema else schema
        kb.row_width = max(schema)
        btns = []

        if all([b == 1 for b in schema]):
            row_btns = (InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
            kb.add(*row_btns)
        else:
            for i in range(len(schema)):
                row_btns = (InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data[:schema[i]])
                kb.row(*row_btns)
                for _ in range(schema[i]):
                    text_and_data.pop(0)
        return kb