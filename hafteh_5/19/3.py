nomre_list = [8,20,19,15,11]

print("list nomre ha : ",nomre_list)

majmoo = 0

for i in nomre_list:
    majmoo+=i

moadel = majmoo/len(nomre_list)
print("moadel: ",moadel)

index_number = 0
for i in nomre_list:
    if i< 10:
        index_number = nomre_list.index(i)
        nomre_list.pop(index_number)
print(nomre_list)
new_majmoo = 0
for i in nomre_list:
    new_majmoo += i

new_moadel = new_majmoo / len(nomre_list)
print("moadel jadid: ",new_moadel)
    
        
