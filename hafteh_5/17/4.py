list_asami = input("list asami ra vared konid: ").split()

list_nomre = list(map(int,input("list nomre ha ra vared konid: ").split()))


print("list asami: ",list_asami)
print("list nomre: ",list_nomre)

for i in range(len(list_asami)):
    list_asami.insert(i+i+1,list_nomre[i])

print(list_asami)
    
    


# حل شده اما نه زياد قشنگ ):
