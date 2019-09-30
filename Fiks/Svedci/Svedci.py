import math

def rozrad(vztahy):
    max_vztahu = 0
    dodavka1 = []
    dodavka2 = []
    for clovek, znamy in vztahy.items():
        if len(znamy) > max_vztahu:
            max_vztahu = len(znamy)

    for vztah_count in range(0, max_vztahu + 1):
        for clovek, znamy in vztahy.items():
            if len(znamy) == vztah_count:
                print("clovek: " +str(clovek))

                print("Pocet_znamych:" + str(len(znamy)))
                print("znamy: "+ str(znamy))
                pocet_znamych_dodavka1 = len(set(znamy) & set(dodavka1))
                pocet_znamych_dodavka2 = len(set(znamy) & set(dodavka2))

                print("pocet znamych v dodavce1: " + str(pocet_znamych_dodavka1))
                print("pocet znamych v dodavce2: " + str(pocet_znamych_dodavka2))

                print("dodavka1: " + str(dodavka1))
                print("dodavka2: " + str(dodavka2))
                print(" ")

                if ((pocet_znamych_dodavka1 > math.floor(vztah_count/2)) & (int(clovek) in dodavka1)) or ((pocet_znamych_dodavka2 > math.floor(vztah_count/2)) & (int(clovek) in dodavka2)):
                    print("fail")
                    return False
                if (pocet_znamych_dodavka1 > pocet_znamych_dodavka2) & (int(clovek) not in dodavka1) & (int(clovek) not in dodavka2):
                    dodavka2.append(int(clovek))

                    if len(znamy) == 1:
                        if int(znamy[0]) not in dodavka1:
                            dodavka1.append(int(znamy[0]))
                elif (int(clovek) not in dodavka1) & (int(clovek) not in dodavka2):
                    dodavka1.append(int(clovek))

                    if len(znamy) == 1:
                        if int(znamy[0]) not in dodavka2:
                            dodavka2.append(int(znamy[0]))
                print("dodavka1: " + str(dodavka1))
                print("dodavka2: " + str(dodavka2))
    return {"dodavka1": dodavka1, "dodavka2": dodavka2}


f = open("input.txt")
w = open("output.txt", "w")
pocet_zadani = f.readline()
for zadani in range(0, int(pocet_zadani)):
    vysledny_string = ""
    svedci = f.readline()
    pocet_svedku, pocet_dvojic_lidi_coseznaji = svedci.split()
    CheckList = {}
    VztahyList = {}
    for svedek in range(1, int(pocet_svedku)+1):
        CheckList[str(svedek)] = False
        VztahyList[str(svedek)] = []

    for dvojice_x in range(0, int(pocet_dvojic_lidi_coseznaji)):
        dvojice = f.readline()
        A, B = dvojice.split()

        VztahyList[str(A)].append(int(B))
        VztahyList[str(B)].append(int(A))
    rozrazeno = rozrad(VztahyList)

    if type(rozrazeno) is not dict:
        vysledny_string = "No solution"
    else:
        for svedek in range(1, int(pocet_svedku) + 1):
            if int(svedek) in rozrazeno["dodavka1"]:
                vysledny_string += "1 "
            else:
                vysledny_string += "2 "
    w.write(vysledny_string+"\n")

    f.readline()
w.close()
f.close()


