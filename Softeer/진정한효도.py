import sys

def sameGround(ground):
    ret=-1
    for i in range(3):
        init=ground[i][0]
        if init==ground[i][1] and init==ground[i][2]:
            return i

    for i in range(3):
        init=ground[0][i]
        if init==ground[1][i] and init==ground[2][i]:
            return i

    return ret


def checkHeight(smallGround):
    cost=100
    
    for i in range(1, 4, 1):
        tmp_cost=0
        for s in smallGround:
            tmp_cost+=abs(s-i)

        cost=min(cost, tmp_cost)

    return cost
    
    
        
ground=[list(map(int, input().split())) for _ in range(3)]

if sameGround(ground)!=-1:
    print(0)
else:
    cost=100
    
    #가로
    for i in range(3):
        cost=min(cost, checkHeight(ground[i]))
        
    #세로
    for i in range(3):
        col_ground=[ground[j][i] for j in range(3)]
        cost=min(cost, checkHeight(col_ground))

                
    print(cost)