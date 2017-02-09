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

    for table in ['energy']:
        cursor.execute('select count(*) from %s' % table)
        row = cursor.fetchone()
        res[table] = row[0]

    return res

@db_decorator
def energy_list(db, cursor, id):
    cursor.execute("""select ts, wh_total
                    from energy
                    where detail_id = %s""",
                    (id, ))

    if cursor.rowcount == 0:
        return None

    fdata = cursor.fetchone()
    
    return rows_to_dict(fdata, cursor.description)