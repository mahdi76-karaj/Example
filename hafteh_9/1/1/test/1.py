file_obj = open("mobile_list_1.txt","r")
data_file = file_obj.read()
print(data_file)

print(10*"_")

#list kardan data bala

list_data = data_file.split("\n")
print("list dat : ",list_data)

print(10*"_")
#khandan be tedad adad ghofteh shodeh
file_obj_1 = open("mobile_list_1.txt","r")
data_file_1 = file_obj_1.read(18)
print(data_file_1)
list_data_file_1 = data_file_1.split("\n")
print("list data1: ",list_data_file_1)

print(12*"_")

#readline

file_obj_2 = open("mobile_list_1.txt","r")
data_file_2 = file_obj_2.readline()
print(data_file_2)
print(12*"_")
# har bar khat badi ra mikhanad
data_file_2_2 = file_obj_2.readline()
print(data_file_2_2)
print(12*"_")

#for ba readline
file = open("mobile_list_1.txt","r")
for i in range(4):
    data_file = file.readline()
    print(data_file)
print(12*"_")
#list dorost kardan ba for ba readline
listdata = []
file_1 = open("mobile_list_1.txt","r")
for i in range(4):
    data = file_1.readline()
    listdata.append(data)
print(listdata)
print(12*"_")
# replace bariae azbian bordan \n
listdata1 = []
file_11 = open("mobile_list_1.txt","r")
for i in range(4):
    data = file_11.readline()
    data_replace = data.replace("\n","")
    listdata1.append(data_replace)
print(listdata1)
print(12*"_")

#readlines
file_11 = open("mobile_list_1.txt","r")
data_file_11 = file_11.readlines()
print(data_file_11)

for mobile in data_file_11:
    print(mobile,end="")







