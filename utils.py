def date_string(date):
    if date is None:
        return ''
    return date.strftime('%Y-%m-%d %H:%M:%S')

def contain_val(val, enum=[]):
    return val in enum

def contain_vals(vals, enum=[]):
    for val in vals:
        if val not in enum:
            return False
    return True

def enumeration(values):
    return ','.join(map(lambda x: '"' + str(x) + '"', values))
