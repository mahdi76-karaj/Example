my_list = [{
    "name": "iphone se 2023",
    "producer": "iphone",
    "price": 800,
    "network": ["gsm", "hsp", "lte", "5g"],
    "size": {"width": 20, "height": 40},
    "ram": 4
},
    {"name": "note 9 pro",
     "producer": "xiaomi",
     "price": 400,
     "network": ["gsm", "hsp", "lte", "5g"],
     "size": {"width": 20, "height": 40},
     "ram": 3
     }
]
for i in range(len(my_list)):
    my_list[i]["ram"] = str(my_list[i]["ram"]) + "gig"

print(f"list strip:{my_list}")
