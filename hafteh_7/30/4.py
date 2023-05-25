my_list = ["Ali", "Reza" ,"Shahram", "Sara"]

my_string = ""

for i in my_list:
    my_string += i + "-"
print(my_string)

my_string_2 = "-".join(my_list)
print(my_string_2)