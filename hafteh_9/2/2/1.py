file = open("file_read.csv","r")
data_file = file.read().split("\n")
print(data_file)
list_dama = []
for i in range(1,len(data_file)):
    n = data_file[i].split(",")
    list_dama.append(n)
print(list_dama)
file =open("file_write.csv","w")
file.write("day"+","+"ave"+"\n")
for i in list_dama:
    sum_dama = 0
    for j in range(1,len(i)):
        sum_dama += int(i[j])
    ave = sum_dama / (len(i)-1)

    file.write(i[0]+","+str(ave)+"\n")

file.close()