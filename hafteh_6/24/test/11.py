mobile_list =[ ["iphonex" , 1000], ["note8", 800], ["A12", 700] ]

sum_price = 0

for mobile in mobile_list:
    for price in mobile[1:]:
        pass
    sum_price += price
    ave = sum_price / len(mobile_list)
    
print("ave is : ",ave)
