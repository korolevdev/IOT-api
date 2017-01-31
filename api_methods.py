import datetime
import MySQLdb
from app import *
from utils import *

def db_decorator(func):
    def f(*args, **kwargs):
        db = get_db()
        cursor = db.cursor()

        try:
            res = func(db, cursor, *args, **kwargs)
        except IntegrityError:
            return False
        cursor.close()
        return res

    return f
