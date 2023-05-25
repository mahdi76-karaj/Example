list_mobile_ha = []


for i in range(3):
    mobile_list = []
    for j in range(3):
        mobile = input("name mobile va gheaimat an ra vared konid: ").split()
        mobile_list.extend(mobile)
        break
    
    list_mobile_ha.append(mobile_list)
    
    for i in range(len(list_mobile_ha)):
        list_mobile_ha[i][1]= int(list_mobile_ha[i][1])
    
    
print(list_mobile_ha)

