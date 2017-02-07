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

@db_decorator
def status(db, cursor):
    res = {}

    print(1)
    for table in ['energy']:
        print(1)
        cursor.execute('select count(*) from %s' % table)
        print(1)
        row = cursor.fetchone()
        print(1)
        res[table] = row[0]

    print(1)
    return res

@db_decorator
def energy_list(db, cursor, id):
    cursor.execute("""select ts, wh_total
                    from energy
                    where device_id = %s""",
                    (id, ))

    if cursor.rowcount == 0:
        return None

    fdata = cursor.fetchone()

    return rows_to_dict(fdata, cursor.description)