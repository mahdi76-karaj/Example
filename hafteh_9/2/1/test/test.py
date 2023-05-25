file_obj = open("mobile_lis_1.csv","r")
data_file = file_obj.read().split("\n")
print(data_file,"\n")

list_mobile = []
for i in range(1,len(data_file)):
    print(data_file[i])
    mobile = data_file[i].split(",")
    print("name: ",data_file[0])
    print("supply: ",data_file[1])
    print("price: ",data_file[2]+"$")
    print(12*"-")
    list_mobile.append(mobile)

print(list_mobile)

file_obj.close()

print(81*"-")

file = open("mobile_lis_2.csv","w")
mobile_name = input("enter mobile name : ")
supply = input("supply: ")
price = input("price: ")
file.write(mobile_name+","+supply+","+price)