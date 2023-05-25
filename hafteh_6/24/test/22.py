list_mobile = []

for j in range(4):
    mobile = []
    for i in range(4):
        model = input("esm va gheimat mobile ra vred konid: ").split("-")
        mobile.extend(model)
        break
    list_mobile.append(mobile)
    
print("list mobile ha va gheimateshan: ",list_mobile)
