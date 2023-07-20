from emoji import emojize

from .constructor import InlineConstructor

def inline_kb_start(telegram_user):
    text = f'{telegram_user.full_name}, \nyou are welcome! \nChoose language:'

    text_and_data = [
        [emojize(':ru: ru', language='alias'), 'btn_ru'],
        [emojize(':england: eng', language='alias'), 'btn_eng'],
    ]
    inline_kb = InlineConstructor.create_kb(text_and_data)
    return text, inline_kb

