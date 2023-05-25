product = {"name":"note 9","price":1000,"producer":"xiaomi"}
print("product name: ",product["producer"])

product_list = [["note 8 pro",200],["iphone",600]]
print(product_list[0][0])
note9 = {
    "name":"note 9 pro",
    "producer":"xiaomi",
    "price": 400,
    "network":["gsm","hsp","lte","5g"],
    "size":{"width":20,"height":40}
}
print(note9["size"])
print(note9["network"][1])
print(note9["name"])

iphone = {
    "name":"iphone se 2023",
    "producer":"iphone",
    "price": 800,
    "network":["gsm","hsp","lte","5g"],
    "size":{"width":20,"height":40}
}
products = [note9,iphone]
print(products)
keyword=iphone.keys()
print(iphone.keys())