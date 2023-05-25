my_list = [{"name": "iphone se 2023","ram": 4},{"name": "note 9 pro","ram": 3 }]
for i in range(len(my_list)):
    print("model mobile: ",my_list[i]["name"])
    pierce = int(input("ple enter pierce of: "))
    my_list[i].update({"price":pierce})

print(my_list)

