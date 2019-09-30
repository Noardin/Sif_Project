f = open("input.txt")

pocet_zadani = f.readline()
for zadani in range(0, int(pocet_zadani)):
    svedci = f.readline()
    pocet_svedku, pocet_dvojic_lidi_coseznaji = svedci.split()
    CheckList={}
    for svedek in range(0, int(pocet_svedku)):
        CheckList[str(svedek)] = False

    for dvojice_x in range(0, int(pocet_dvojic_lidi_coseznaji)):
        dvojice =f.readline()

        print(dvojice)

    f.readline()
f.close()

