nomre_list = [8,20,19,15,11]
print(nomre_list)
majmoo = 0
for i in nomre_list:
    majmoo+=i
avg = majmoo/len(nomre_list)
print("moadel: ",avg)

for i in nomre_list:
    if i <= 10:
        nomre_list.remove(i)
print(nomre_list)
new_majmoo = 0
for i in nomre_list:
    new_majmoo += i
    
new_avg = new_majmoo / len(nomre_list)
print("moadel jadid: ",new_avg)
        
