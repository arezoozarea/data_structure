def recur(cur_dict, keys_input):
    cur_dict = {}
    value_input = {"university": "harward", "entery_date": 2005}
    keys = keys_input.split(".")
    if len(keys) <= 1:
        cur_dict[keys.pop(0)] = value_input
        return cur_dict
    key = keys.pop(0)
    cur_dict[key] = {}
    recur(cur_dict, keys_input)
    return cur_dict
