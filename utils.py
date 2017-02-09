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

def rows_to_dict(rows, description, remove=[]):
    res = {}
    for key, val in enumerate(rows):
        field = description[key][0]

        if field[0:2] == 'is':
            val = bool(val)
        if field == 'date':
            val = date_string(val)
        if field in remove:
            continue

        res[field] = val

    return res

def enumeration(values):
    return ','.join(map(lambda x: '"' + str(x) + '"', values))
