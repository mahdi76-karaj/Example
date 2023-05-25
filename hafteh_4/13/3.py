list_nomre_az_20 = list(map(float,input("nomre ha ra vared konid(az 20 nomre): ").split()))
list_nomre_az_10 = []
for i in range(len(list_nomre_az_20)):
    nomre_az_10 = list_nomre_az_20[i]*10/20
    list_nomre_az_10.append(nomre_az_10)

print(list_nomre_az_10)
    
    
