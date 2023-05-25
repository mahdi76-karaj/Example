while True:

    def cla_ghiamat_jadid(ghiamat_kala, darsad_tavarom=0.1):
        ghiamat_jadid_kala = ghiamat_kala + (ghiamat_kala * darsad_tavarom)
        print(f"ghiamat jadid kala :{ghiamat_jadid_kala}")
        return  ghiamat_jadid_kala,darsad_tavarom

    user_input = list(map(float, input("enter ghiamat kala and darsad tavarom: ").split()))
    if len(user_input) == 2:
        print(cla_ghiamat_jadid(user_input[0], user_input[1]))
    elif len(user_input) == 1:
        print(cla_ghiamat_jadid(user_input[0]))
    else:
        print("wrong input")
    status = input("aya edameh midahid(y/n):")
    if status == "n":
        break
