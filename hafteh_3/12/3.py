kar_list =["tamas ba doctor", "tamiz kardan otagh", "motalee"]
print("kar_list:",kar_list)
kar_time_list = []
majmoo_time = 0
for kar in kar_list:
    anjam_dadan_kar = input(f"aya {kar} anjam shod(y/n)? ")
    if anjam_dadan_kar == "y":
        zaman_anjam_kar = int(input(f"zaman anjam {kar} cheghadr bod(min)? "))
        kar_time_list.append(zaman_anjam_kar)
    elif anjam_dadan_kar == "n":
        pass
    else:
        print("vorodi eshtebah vared kardid")
print("kar time list: ",kar_time_list)

for i in range(len(kar_time_list)):
    majmoo_time += kar_time_list[i]

print("majmoo zaman anjam kar",majmoo_time,"min bode ast")
        
    
