jensiat = input("jensiat(mard/zan): ")
sen = int(input("sen: "))
vaziat_tahsil = input("vaziat tahsil(y/n): ")

if jensiat == "mard" and sen > 18 and vaziat_tahsil == "n":
    print("mashmool")
else:
    print("mashmool nistid")
