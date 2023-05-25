list_saf = input("list_saf ra vared koind: ").split()
list_saf_1 = []
for name in range(len(list_saf)):
    n = ((str(name + 1) + "_" + list_saf[name]))
    m = list_saf[name].replace(list_saf[name],n)
    list_saf_1.append(m)


my_string = ""
for i in list_saf_1:
    my_string += " " + i
print("saf list: ",my_string)




