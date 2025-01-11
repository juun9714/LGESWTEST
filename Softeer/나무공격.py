import sys

def countEvil(forest):
    count=0
    for i in range(0, n, 1):
        for j in range(0, m, 1):
            if forest[i][j]==1:
                count+=1
    return count
    

n, m = map(int, input().split())
forest=[list(map(int, input().split())) for _ in range(n)]
L_1, R_1 = map(int, input().split())
L_2, R_2 = map(int, input().split())


for i in range(L_1-1, R_1, 1):
    for j in range(0, m, 1):
        if forest[i][j]==1:
            forest[i][j]=0
            break

for i in range(L_2-1, R_2, 1):
    for j in range(0, m, 1):
        if forest[i][j]==1:
            forest[i][j]=0
            break

print(countEvil(forest))