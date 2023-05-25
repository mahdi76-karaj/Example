my_list = [{
    "name":"             iphone se 2023          ",
    "producer":"iphone",
    "price": 800,
    "network":["gsm","hsp","lte","5g"],
    "size":{"width":20,"height":40}
},
{   "name":"            note 9 pro                ",
    "producer":"xiaomi",
    "price": 400,
    "network":["gsm","hsp","lte","5g"],
    "size":{"width":20,"height":40}}
]
print(f"list avaleh{my_list}")
for i in range(len(my_list)):
    my_list[i]["name"] = my_list[i]["name"].strip()

print(f"list strip:{my_list}")
