maxX = 10
maxY = 8

Silnice = [[[0,0,0,0] for r in range(maxX)] for s in range(maxY)]
XYcil = [5,6]
XYstart = [1,2]
Silnice[XYcil[1]][XYcil[0]] = [1,1,1,1] #1 for cil
Silnice[XYstart[1]][XYcil[0]] = [2,2,2,2] #2 for start

#5 for auto

def TurnRight(XYauto):
    index = Silnice[XYauto[1]][XYauto[0]].index(5)
    newXYauto = []
    



print(Silnice[1][1])
