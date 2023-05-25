product_list = [
    {"name":"iphone 13pro","producer":"apple","price":11000,"network":["gsm","lte","5g"],"ram":6},
    {"name":"12t pro","producer":"xiaomi","price":800,"network":["gsm","lte","5g"],"ram":8 }]
deleted_rams = []

print("product list is: ",product_list)

for item in range(len(product_list)):
    deleted_ram = product_list[item].pop("ram")
    deleted_rams.append(deleted_ram)
print("deleted ram: ",deleted_rams)
print("new product list is: ",product_list)





