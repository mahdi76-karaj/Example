d = {"one": 1, "two": 2, "four": 4, "three": 3}


def value_returner(dic):
    value_list = []
    for key,value in dic.items():
        print(key,value)
        value_list.append(value)
    return value_list


print("value list: ",value_returner(d))
