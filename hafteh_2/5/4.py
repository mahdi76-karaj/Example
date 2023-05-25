while True:
    soraat_be_km = int(input("saraat be km/h: "))
    zaman_be_min = int(input("zaman in minutes: "))
    masafat_tei_shodeh = (soraat_be_km * (zaman_be_min/60))

    if masafat_tei_shodeh > 100:
        print("az mahdodeh kharej shodid")
    else:
        print("az mahdideh kharej nashodid")
