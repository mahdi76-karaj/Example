names_list = ["maryam","ali","ali","ali","reza","maryam","reza","reza","reza","ali"]
print("list esm ha: ",names_list)
counter_ali=0
counter_maryam=0
counter_reza=0
revers_names_list = []
for i in range(len(names_list)-1,-1,-1):
    revers_names_list.append(names_list[i]) 
print(revers_names_list)

names_list.clear()
user_input=input("akhrin esm che kasi ra mikhahid hazf konid: ")
#print(names_list)

for i in range(len(revers_names_list)):
    if revers_names_list[i] == user_input :
        revers_names_list.remove(revers_names_list[i])
        break
    


for i in range(len(revers_names_list)-1,-1,-1):
   names_list.append(revers_names_list[i])
print(names_list)
    
 
    
for i in range(len(names_list)):
    if names_list[i] == "maryam":
        counter_maryam += 1
    elif names_list[i] == "reza":
        counter_reza += 1
    elif names_list[i] == "ali":
        counter_ali += 1

if "ali" in names_list:
    print("ali: ",counter_ali)

if "maryam" in names_list:
    print("maryam: ",counter_maryam)

if "reza" in names_list:
    print("reza: ",counter_reza)


if "maryam" in names_list :
    if (counter_maryam > counter_ali) and (counter_maryam > counter_reza):
        print("maryam barandeh shod ")

if "ali" in names_list :
    if (counter_ali > counter_maryam) and (counter_ali > counter_reza):
        print("ali barande shod ")

if "reza" in names_list :
    if (counter_reza > counter_maryam) and (counter_reza > counter_ali):
        print("reza barandeh shod ")


        
























##names_list = ["ali","mahdi","ali","mahdi","reza","ali"]  
##for i in range(len(names_list)-1,-1,-1):
##    print(names_list[i])
        

