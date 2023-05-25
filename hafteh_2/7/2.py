barani_bodan_hava = input("aya hava barani ast(y/n): ")
dama = int(input("dama hava cheghadr ast: "))
standard_bodan_zamin = input("aya zamin bazi standard ast(y/n): ")

if ( barani_bodan_hava == "y" or dama < 0 ) and standard_bodan_zamin == "n" :
    print("bazi cancel")
else:
    print("ok")
