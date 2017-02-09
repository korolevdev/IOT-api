import MySQLdb
from flask import request
from app import *
from wrappers import *
from utils import *
from api_methods import *

@app.route('/status/', methods=['GET'])
def url_status():
    response = status()
    return response_wrap(response)

@app.route('/energy/list/', methods=['GET'])
def url_energy_list():
    id = request.args.get('id')
    response = energy_list(id)
    return response_wrap(response)