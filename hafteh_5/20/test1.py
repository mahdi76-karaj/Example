mylist=["maryam","ali","mahdi","ali","hasan"]
user_input = input(": ")


##for i in range(len(mylist)):
##    try:
##        mylist.remove("ali")
##    except:
##        print("ali ha hame hazf shodand")
##        break
##print(mylist)

for i in range(len(mylist)):
    if mylist[i] == user_input:
        mylist.remove(mylist[i])
        break
print(mylist)
