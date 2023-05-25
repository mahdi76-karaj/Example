#  خوندن فایل و لیست کردن شون
file_obj = open("myfile.csv","r+")
data = file_obj.read().split("\n")

# دوباره لیست کردن اطلاعات
list_data = []
for i in range(1,len(data)-2):
    n = data[i].split(",")
    list_data.append(n)
print(list_data)

# دیکشنری کردن خط به خط اصلاعات
new_list = []
for item in list_data:
    my_dict = {}
    my_dict.update({item[0]:item[1:]})
    new_list.append(my_dict)
print(new_list)

# دریافت وردوی برای ویرایش یا اضافه کردن اطلاعات
while True:
    status = input("ketab vared mikonid(y/n): ").lower()
    if status == "y":
        book_name = input("book name: ").lower()
        price = input("price: ")
        supply = input("supply: ")
        isbn = input("isbn: ")

        for item in new_list:
            for i in item:
                if i == book_name:
                    item.update({book_name: [price, supply, isbn]})
                    break
                else:
                    n = {book_name: [price, supply, isbn]}
                    new_list.append(n)
                    break
            break
    else:
        break
print(new_list)

# تبدیل کردن دیکشنری ها به تاپل
new_list_2 = []
for item in new_list:
    resultlist = list(item.items())
    new_list_2.append(resultlist)
print(new_list_2)

# تبدیل کردن تاپل ها به لیست
new_list_3 = []

for item in new_list_2:
    for i in item:
        n = (list(i))
        new_list_3.append(n)
print(new_list_3)

# تبدیل کردن لیست ها به استرینگ
new_string = ""
for item in new_list_3:
    new_string = new_string + item[0]+","
    s = " ".join(str(x) for x in item[1])
    s_2 = s.replace(" ",",")
    new_string = new_string + s_2 + "\n"
print(new_string)

# و در نهایت نوشتن داده ها درست شده به فایل
file_obj = open("myfile.csv","w+")
new_data = file_obj.write("bookname,price,supply,isbn\n")
file_obj.close()
file_obj = open("myfile.csv","a+")
new_data2 = file_obj.write(new_string)
file_obj.close()
