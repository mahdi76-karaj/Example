mysaf = []

while True:
    user_input = input("vorodi khod ra vared konid: ")
    if user_input == "check":
        shomare = input("shomareh khod ra vared konid: ")
        if shomare in mysaf:
            print("jayghahe shoma ",mysaf.index(shomare)+1,"ast")
            break
        else:
            print("shomareh shoma vojod nadarad")
            break
        
    else:
        mysaf.append(user_input)
        print(mysaf)

        
