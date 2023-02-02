from database.db import *

@db_session
def register_user(telegram_user):
    if not User.exists(tg_id = telegram_user.id):
        user = User(
            tg_id=telegram_user.id, 
            username=telegram_user.username, 
            first_name=telegram_user.first_name, 
            last_name=telegram_user.last_name)
        flush()
        return user
    else:
        print(f'User {telegram_user.id} exists')

@db_session
def get_user(telegram_user):
    return User.get(tg_id=telegram_user.id)

@db_session
def get_users():
    return User.select(int(u.tg_id) for u in User)
        
@db_session()
def update_user(
    tg_id : int, 
    username : str = None,
    first_name : str = None,
    last_name : str = None,
    is_banned : bool = None
    ):

    user_to_update = User.get(tg_id = tg_id)
    if username:
        user_to_update.username = username
    if first_name:
        user_to_update.first_name = first_name
    if last_name:
        user_to_update.last_name = last_name
    if is_banned:
        user_to_update.is_banned = is_banned
    if is_banned == False:
        user_to_update.is_banned = is_banned
