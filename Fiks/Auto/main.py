from queue import Queue
maxX = 10
maxY = 8
q = Queue()
Silnice = [[[0,0,0,0] for r in range(maxX)] for s in range(maxY)]
XYcil = [5,0]
XYstart = [0,0]
Silnice[XYcil[1]][XYcil[0]] = [-1,-1,-1,-1] #-1 for cil
Silnice[XYstart[1]][XYcil[0]] = [1,1,1,1] #1 for start

d = {
    "End":False,
    "newDirection":0,
    "state":1,
    "Silnice": Silnice,
    "newXYauto": XYstart
}
# direction == 0 == ^
# direction == 1 == >
# direction == 2 == v
# direction == 3 == <

def findPath():
    while True:
        p = q.get()
        if p["End"]:
            for y in p["Silnice"]:
                print(str(y))
            return p["state"]
        TurnRight(p["newXYauto"], p["newDirection"], p["state"], p["Silnice"])
        Streight(p["newXYauto"], p["newDirection"], p["state"], p["Silnice"])
        q.task_done()




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
    print("pristi poloha: "+str(pristiPoloha))
    if ((pristiPoloha < state+1) & (pristiPoloha != -1) & (pristiPoloha != 0)) | (pristiPoloha == -2):
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
    print("pristi poloha: " + str(pristiPoloha))
    if ((pristiPoloha < state+1) & (pristiPoloha != -1) & (pristiPoloha != 0)) | (pristiPoloha == -2):
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


q.put(d)
print(str(findPath()))
