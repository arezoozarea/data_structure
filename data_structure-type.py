# mydict = {}
# keys = ['a', 'b', 'c']
# value = [{"university": "harward", "entery_date": 2005}]
# input_data = "experiences.educations", [{"university": "harward", "entery_date": 2005}]
mydict = {}
keys_input=["experiences","educations"]
value_input = [{"university": "harward", "entery_date": 2005}]
def recur(cur_dict, keys_input):
    if len(keys_input) <= 1:
        cur_dict[keys_input.pop(0)] = value_input
        return cur_dict
    key = keys_input.pop(0)
    cur_dict[key] = {}
    recur(cur_dict[key], keys_input)
    return cur_dict


print(recur(mydict, keys_input))
# structure_type("experiences.educations", [{"university": "harward", "entery_date": 2005}])
