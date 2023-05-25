soraat = int(input("soraat: "))
vaziat_hava= input("aya hava barani ast (y/n): ")
if vaziat_hava == "y":
    if soraat > 80 :
        print("jarimeh shodid")
    else:
        print("jarimeh nashodid")
elif vaziat_hava == "n":
    if soraat > 100:
        print("jarimeh shodid")
    else:
        print("jarimeh nashodid")
