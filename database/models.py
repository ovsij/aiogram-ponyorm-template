from datetime import datetime
from decimal import Decimal
from pony.orm import *

db = Database()


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    tg_id = Required(Decimal, unique=True)
    username = Optional(str, unique=True)
    first_name = Optional(str, nullable=True)
    last_name = Optional(str, nullable=True)
    was_registered = Optional(datetime, default=lambda: datetime.now())
    is_banned = Optional(bool, default=False)


class Product(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)


    