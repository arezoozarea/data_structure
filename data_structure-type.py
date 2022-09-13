def is_list_type(last_value):
    return type(last_value)== list



mydict = {}


def recur(keys_input, cur_dict, last_value):
    if len(keys_input) <= 1:
        last_key = keys_input[0]
        if is_list_type(last_value):
            if last_key not in cur_dict:
                cur_dict[last_key] = []
            for item in last_value:
                cur_dict[last_key].append(item)
            return cur_dict
    key = keys_input.pop(0)
    if key not in cur_dict:
        cur_dict[key] = {}
    recur(keys_input, cur_dict[key], last_value)
    return cur_dict


def structure_type(paths, last_value):
    key_inputs = paths.split(".")
    return recur(key_inputs, mydict, last_value)


structure_type("experiences.educations", [{"university": "harward", "entery_date": 2005}])
structure_type("experiences.educations", [{"university": "oxford", "entery_date": 2011}])
structure_type("experiences.educations", [{"university": "birmangham", "entery_date": 2007}])
print(mydict)
