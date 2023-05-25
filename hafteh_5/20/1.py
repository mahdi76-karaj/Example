names_list =["maryam","ali","reza","maryam","reza","reza","ali"]
print(names_list)
ali_counter = 0
maryam_counter = 0
reza_counter = 0
user_input=input("che kasi takhalof kard(maryam/reza/ali): ")

for i in range(len(names_list)):
    if user_input not in names_list:
        print("vorodi shtebahi vared kardid ")
        break

for i in range(len(names_list)):
    try :
        names_list.remove(user_input)
    except:
        break
    
print(names_list)

for i in range(len(names_list)):
    if names_list[i]=="maryam":
        maryam_counter += 1
    elif names_list[i]== "reza":
        reza_counter += 1
    elif names_list[i]=="ali":
        ali_counter += 1

if "ali" in names_list:
    print("ali: ",ali_counter)

if "maryam" in names_list:
    print("maryam: ",maryam_counter)

if "reza" in names_list:
    print("reza: ",reza_counter)


if "maryam" in names_list :
    if (maryam_counter > ali_counter) and (maryam_counter > reza_counter):
        print("maryam barandeh shod ")

if "ali" in names_list :
    if (ali_counter > maryam_counter) and (ali_counter > reza_counter):
        print("ali barande shod ")

if "reza" in names_list :
    if (reza_counter > maryam_counter) and (reza_counter > ali_counter):
        print("reza barandeh shod ")

        
