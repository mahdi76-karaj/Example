list_nomreh_class1 = list(map(int,input("list nomreh class 1 ra vared konid:").split("-")))

list_nomreh_class2 = list(map(int,input("list nomreh class 2 ra vared konid: ").split("-")))

print("list nomreh class1: ",list_nomreh_class1)

print("list nomreh class2: ",list_nomreh_class2)


list_nomreh_2_class = list_nomreh_class1

list_nomreh_class1.extend(list_nomreh_class2)

list_moratab_shodeh = sorted(list_nomreh_2_class)

print("list moratab shodeh: ",list_moratab_shodeh)

print("list nomreh har 2 class:  ",list_nomreh_2_class)
