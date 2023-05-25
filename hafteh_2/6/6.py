soraat = int(input("soraat: "))
vaziat_hava = input("aya hava barani ast(y/n): ")

if vaziat_hava == "y" and soraat > 80 or vaziat_hava == "n" and soraat > 100 :
    print("jarimeh shodid")
else:
    print("jarimeh nashodid")
