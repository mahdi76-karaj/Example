saf_list = ["shahram","mohammad","ali","sara","sara","reza","ali","ali","reza","sara","ali"]

print("saf: ",saf_list)

shahram_counter = 0
shahram_counter_dovom = 0

mohammad_counter = 0
mohammad_counter_dovom = 0

ali_counter = 0
ali_counter_dovom = 0

sara_counter = 0
sara_counter_dovom = 0

reza_counter = 0
reza_counter_dovom = 0

for i in range(len(saf_list)):
    
    if saf_list[i] == "shahram":
        shahram_counter += 1
        if shahram_counter > 1:
            for i in range(len(saf_list)):
                if saf_list[i] == "shahram":
                    shahram_counter_dovom += 1
                    saf_list[i] = "shahram" + str(shahram_counter_dovom)

    elif saf_list[i] == "mohammad":
        mohammad_counter += 1
        if mohammad_counter > 1:
            for i in range(len(saf_list)):
                if saf_list[i] == "mohammad":
                    mohammad_counter_dovom += 1
                    saf_list[i] = "mohammad" + str(mohammad_counter_dovom)


    elif saf_list[i] == "ali":
        ali_counter += 1
        if ali_counter > 1:
            for i in range(len(saf_list)):
                if saf_list[i] == "ali":
                    ali_counter_dovom += 1
                    saf_list[i] = "ali" + str(ali_counter_dovom)

    elif saf_list[i] == "sara":
        sara_counter += 1
        if sara_counter > 1:
            for i in range(len(saf_list)):
                if saf_list[i] == "sara":
                    sara_counter_dovom += 1
                    saf_list[i] = "sara" + str(sara_counter_dovom)

    elif saf_list[i] == "reza":
        reza_counter += 1
        if reza_counter > 1:
            for i in range(len(saf_list)):
                if saf_list[i] == "reza":
                    reza_counter_dovom += 1
                    saf_list[i] = "reza" + str(reza_counter_dovom)





        
print("saf jadid: ",saf_list)
