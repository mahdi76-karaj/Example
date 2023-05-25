file_2_obj = open("file_2.txt","r")
data_file_2 = file_2_obj.readlines()
#print(data_file_2)

list_to_dar_to = []
for i in data_file_2:
    n = i.replace("\n","")
    m = n.split("-")
    list_to_dar_to.append(m)
print("list class: ",list_to_dar_to)

sum_nomreh = 0
for j in range(len(list_to_dar_to)):
    sum_nomreh += int(list_to_dar_to[j][-1])
ave = sum_nomreh / len(list_to_dar_to)
print("ave is: ",ave)
