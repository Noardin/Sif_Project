from queue import Queue

# direction == 0 == ^
# direction == 1 == >
# direction == 2 == v
# direction == 3 == <


def findPath():
    while True:
        p = q.get()
        if p["End"]:
            return int(p["state"])-1
        TurnRight(p["newXYauto"], p["newDirection"], p["state"], p["Silnice"])
        Streight(p["newXYauto"], p["newDirection"], p["state"], p["Silnice"])
        q.task_done()
        if q.empty():
            return "No solution"


def TurnRight(XYauto, direction, state, Silnice):
    End =False
    newXYauto = []
    if direction == 0:
        newXYauto.append(XYauto[0] + 1)
        newXYauto.append(XYauto[1])
    if direction == 1:
        newXYauto.append(XYauto[0])
        newXYauto.append(XYauto[1]-1)
    if direction == 2:
        newXYauto.append(XYauto[0]-1)
        newXYauto.append(XYauto[1])
    if direction == 3:
        newXYauto.append(XYauto[0])
        newXYauto.append(XYauto[1]+1)

    if direction !=3:
        newDirection = direction+1
    else:
        newDirection = 0
    if (newXYauto[0] > maxX-1) | (newXYauto[1] > maxY-1) | (newXYauto[0] < 0) | (newXYauto[1] < 0):

        return False
    pristiPoloha = Silnice[newXYauto[1]][newXYauto[0]][newDirection]

    if ((pristiPoloha < state+1) & ((pristiPoloha != -1) & (pristiPoloha != 0))) | (pristiPoloha == -2):
        return False

    if pristiPoloha == -1:
        End = True

    Silnice[newXYauto[1]][newXYauto[0]][newDirection] = state+1
    d = {
        "End": End,
        "Silnice": Silnice,
        "newXYauto": newXYauto,
        "newDirection": newDirection,
        "state": state+1
    }
    q.put(d)
    return d

def Streight(XYauto, direction, state, Silnice):
    newXYauto = []
    End= False
    if direction == 0:
        newXYauto.append(XYauto[0])
        newXYauto.append(XYauto[1]+1)
    if direction == 1:
        newXYauto.append(XYauto[0]+1)
        newXYauto.append(XYauto[1])
    if direction == 2:
        newXYauto.append(XYauto[0])
        newXYauto.append(XYauto[1]-1)
    if direction == 3:
        newXYauto.append(XYauto[0]-1)
        newXYauto.append(XYauto[1])
    newDirection = direction
    if (newXYauto[0] > maxX-1) | (newXYauto[1] > maxY-1) | (newXYauto[0] < 0) | (newXYauto[1] < 0):

        return False

    pristiPoloha = Silnice[newXYauto[1]][newXYauto[0]][newDirection]
    if ((pristiPoloha < state+1) & ((pristiPoloha != -1) & (pristiPoloha != 0))) | (pristiPoloha == -2):
        return False
    if pristiPoloha == -1:
        End = True

    Silnice[newXYauto[1]][newXYauto[0]][newDirection] = state + 1
    d = {
        "End": End,
        "Silnice": Silnice,
        "newXYauto": newXYauto,
        "newDirection": newDirection,
        "state": state + 1
    }
    q.put(d)
    return d

maxX = 10
maxY = 8


XYcil = [5,5]
XYstart = [0,0]


f = open("input.txt")
pocet_zadani = f.readline()
vysledky = []
for z in range(int(pocet_zadani)):
    q = Queue()
    maxX, maxY, K = f.readline().split()
    maxX = int(maxX)
    maxY = int(maxY)
    Xstart,Ystart, Xcil, Ycil = f.readline().split()
    XYstart = [int(Xstart)-1, int(Ystart)-1]
    XYcil = [int(Xcil)-1, int(Ycil)-1]
    Silnice = [[[0, 0, 0, 0] for r in range(int(maxX))] for s in range(int(maxY))]
    Silnice[XYcil[1]][XYcil[0]] = [-1, -1, -1, -1]  # -1 for cil
    Silnice[XYstart[1]][XYstart[0]] = [1, 1, 1, 1]  # 1 for start
    for k in range(int(K)):
        x,y = f.readline().split()
        Silnice[int(y)-1][int(x)-1] = [-2, -2, -2, -2]

    d = {
        "End": False,
        "newDirection": 0,
        "state": 1,
        "Silnice": Silnice,
        "newXYauto": XYstart
    }
    q.put(d)
    vysledky.append(str(findPath()))

w = open("output.txt","w")
for i, v in enumerate(vysledky):
    w.write(v)
    if i < int(pocet_zadani)-1:
        w.write("\n")