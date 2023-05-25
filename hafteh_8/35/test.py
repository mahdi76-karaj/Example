product_list = [
    {"name": "iphone 13pro", "producer": "apple", "price": 11000, "network": ["gsm", "lte", "5g"], "ram": 6},
    {"name": "12t pro", "producer": "xiaomi", "price": 800, "network": ["gsm", "lte", "5g"], "ram": 8}]
print(product_list[1].pop("ram"))

print(product_list)
product_list[0]["year"] = 2022
print(product_list)
product_list[0].popitem()
print(product_list)
del product_list[0]
print(product_list)
del product_list
# print(product_list)
product_list = [
    {"name": "iphone 13pro", "producer": "apple", "price": 11000, "network": ["gsm", "lte", "5g"], "ram": 6},
    {"name": "12t pro", "producer": "xiaomi", "price": 800, "network": ["gsm", "lte", "5g"], "ram": 8}]
print(product_list)
print(product_list[0]["ram"])
