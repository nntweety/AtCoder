X, Y, Z = map(int, input().split())

ABC_BOX = [X, Y, Z]

ABC_BOX[0], ABC_BOX[1] = ABC_BOX[1], ABC_BOX[0]
ABC_BOX[0], ABC_BOX[2] = ABC_BOX[2], ABC_BOX[0]

print(str(ABC_BOX[0]) + ' ' + str(ABC_BOX[1]) + ' ' + str(ABC_BOX[2]))