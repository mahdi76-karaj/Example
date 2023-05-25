names_list = ["maryam","ali","ali","ali","reza","maryam","reza","reza","reza","ali"]
print("list esm ha: ",names_list)
user_input=input("dovomin esm che kasi ra mikhahid hazf konid: ")

counter_ali=0
counter_maryam=0
counter_reza=0

for i in range(len(names_list)):
    if user_input == "ali":
        if names_list[i] == "ali":
            counter_ali +=1
            if counter_ali == 2:
                names_list.pop(i)
                break
    elif user_input == "maryam":
        if names_list[i] == "maryam":
            counter_maryam +=1
            if counter_maryam == 2:
                names_list.pop(i)
                break
    elif user_input == "reza":
        if names_list[i] == "reza":
            counter_reza +=1
            if counter_reza == 2:
                names_list.pop(i)
                break
print("list jadid esm ha: ",names_list)

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
