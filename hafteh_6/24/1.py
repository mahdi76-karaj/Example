list_mobile = [["iphone",1000],["note8",800],["a12",700]]

majmoo_gheimat_mobile_ha = 0

for mobile in range(len(list_mobile)) :
    majmoo_gheimat_mobile_ha += list_mobile[mobile][1]
    mianghin = majmoo_gheimat_mobile_ha / len(list_mobile)
print("mianghin gheimat mobile ha",mianghin)

##sum_price = 0
##for mobile in list_mobile :
##    for price in mobile[1:]:
##        pass
##
##    sum_price += price
##    ave = sum_price / len(list_mobile)
##print("ave is: ",ave)
