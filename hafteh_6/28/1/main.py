from convert import tabdil_dama ,tabdil_meter
while True:
    dastor = input("enter input(dama/meter): ")
    if dastor == "dama":
        dama = int(input("enter dama(cintigerad): "))
        print("dama barabar ba ",tabdil_dama(dama),"farenhide ast")
    elif dastor == "meter":
        meter = int(input("enter tol(mile): "))
        print("tol barabar ba",tabdil_meter(meter),"meter ast")