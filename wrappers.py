from flask import jsonify

OK = 0
NOT_FOUND = 1
INVALID = 2
UNCORRECT = 3
UNKNOWN = 4
USER_EXISTS = 5

def response_wrap(response, code=OK):
    return jsonify({
        'code': code,
        'response': response
        })

def response_not_found(response):
    return response_wrap(response, NOT_FOUND)

def response_invalid(response):
    return response_wrap(response, INVALID)

def response_uncorrect(response):
    return response_wrap(response, UNCORRECT)

def response_unknown(response):
    return response_wrap(response, UNKNOWN)

def response_user_exists(response):
    return response_wrap(response, USER_EXISTS)
