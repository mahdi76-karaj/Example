sorfeh = input("aya sorfeh mikonid(y/n): ")
tanghieh_nafas = input("aya tnghieh nafas darid(y/n): ")
dama_badan = float(input("dama badan shoma cheghadr ast: "))

if sorfeh == "y" and tanghieh_nafas == "y" and dama_badan > 37.5:
    print("Bimari noeh 1")
elif sorfeh == "y" and tanghieh_nafas == "y" and dama_badan <= 37.5 :
    print("Bimarie noeh 2")
else:
    print("shoma bimar nistid")
