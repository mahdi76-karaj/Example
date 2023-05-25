mobiles = [{
    "name":"iphone se 2023",
    "producer":"iphone",
    "price": 800,
    "network":["gsm","hsp","lte","5g"],
    "size":{"width":20,"height":40}
},
{    "name":"note 9 pro",
    "producer":"xiaomi",
    "price": 400,
    "network":["gsm","hsp","lte","5g"],
    "size":{"width":20,"height":40}}
]
print(mobiles)
for i in range(len(mobiles)):
    percent = int(input("enter percent of increasment: "))
    last_price = mobiles[i]["price"]
    new_price = (100+percent)*last_price/100
    mobiles[i]["price"] = new_price
    print(mobiles)