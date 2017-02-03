import MySQLdb
from flask import request
from app import *
from wrappers import *
from utils import *
from api_methods import *

@app.route('/energy/list/', methods=['GET'])
def url_energy_list():
    id = request.args.get('id')

    fdata = forum_data(id)
    if fdata:
        return response_wrap(fdata)
    else:
        return response_not_found("Id %s doesn't exist" % forum)