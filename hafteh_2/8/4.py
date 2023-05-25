nobat = 1
eshtebah_1 = 0
eshtebah_2 = 0
while True :
    if nobat % 2 != 0:
        nafar1 = int(input("nafar1: "))
        if nobat % 5 == 0 and nafar1 != "Hop":
            eshtebah_1 += 1
            print("khata: nafar1",eshtebah_1,"khata")
            if eshtebah_1 >= 3:
                print("nafar2 barandeh shod")
                break
            
    elif nobat % 2 == 0:
        nafar2 = int(input("nafar2: "))
        if nobat % 5 == 0 and nafar2 != "Hop":
            eshtebah_2 += 1
            print("khata: nafar2",eshtebah_2,"khata")
            if eshtebah_2 >= 3:
                print("nafar1 barandeh shod")
                break








    nobat += 1
    
