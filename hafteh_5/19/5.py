numbers_list=[]
for i in range(1,101):
    numbers_list.append(i)

print("list adad: ",numbers_list,"\n")

for i in numbers_list:
    if i % 5 == 0:
        numbers_list.remove(i)
print("list adad jadid: ",numbers_list,"\n")
