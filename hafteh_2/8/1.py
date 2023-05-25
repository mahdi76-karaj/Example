ghemat_be_dollar = int(input("ghemat dollar: "))

while True:
    ghemat_mahsol_be_dollar = int(input("ghemat kala ra be dollar vared konid: "))

    tabdil_ghemat_mahsol_be_roman = ghemat_mahsol_be_dollar * ghemat_be_dollar

    print("ghemat mahsol be toman = ",tabdil_ghemat_mahsol_be_roman)

    edame = input("aya edame midahid(y/n)? ")

    if edame == "n":
        print("payan")
        break
    
