# mydict = {}
# keys = ['a', 'b', 'c']
# value = [{"university": "harward", "entery_date": 2005}]
# input_data = "experiences.educations", [{"university": "harward", "entery_date": 2005}]
# mydict = {}
# keys_input = ["experiences", "educations"]
# value_input = [{"university": "harward", "entery_date": 2005}]
mydict = {}

def recur(keys_input, cur_dict, last_value):
    if len(keys_input) <= 1:
        cur_dict[keys_input.pop(0)] = last_value
        return cur_dict
    key = keys_input.pop(0)
    cur_dict[key] = {}
    recur(keys_input, cur_dict[key], last_value)
    return cur_dict


def structure_type(paths, last_value):
    key_inputs = paths.split(".")
    return recur(key_inputs, mydict, last_value)


structure_type("experiences.educations", [{"university": "harward", "entery_date": 2005}])
structure_type("experiences.educations", [{"university": "oxford", "entery_date": 2011}])

print(mydict)
