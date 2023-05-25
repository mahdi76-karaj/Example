new_dic = {"name":"mahdi","code_meli":"03115945811"}
# اضافه کردن ایتم
new_dic["tarikh tavalod"] = "1997"
print(new_dic)

#اضافه کردن یک دیکشنری به عنوان یه ایتم جدید
new_dic["location"]= {"mahal tavalod":"karaj","mahal sodor":"karaj"}
print(new_dic)
# عوض کردن یک ایتم
new_dic["name"]="pooneh"
print(new_dic)
#key error
#print(new_dic["tahsilat"])
# تغیر دادن و اضافه کردن با اپدیت
new_dic.update({"name":"reza","esm pedar":"mansor"})
print(new_dic)

##########################################################

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

while True:
    break_ = input("aya mikhahid edameh dahid(y/n): ")
    if break_ == "y":
        name = input("enter name of new mobile: ")
        price = int(input("enter price: "))
        new_mobile = {"name": name, "price": price}
        mobiles.append(new_mobile)
        print(f"list mobile :\n {mobiles}")
    else:
        print(mobiles)
        break




