list_namoratab = ["blue","water","apple","park","book","bee","car"]
print("list naboratab: ",list_namoratab)
list_namoratab.sort()
#print(list_namoratab)
list_moratab_shodeh = input("list ba ra moratab shode vared konid: ").split()

for i in range(len(list_moratab_shodeh)) :
    if list_moratab_shodeh[i] == list_namoratab[i]:
        print("barandeh shodid (: ")
        break
    else:
        print("bakhtid ):")
        break
        
