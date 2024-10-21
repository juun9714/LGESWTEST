#https://www.acmicpc.net/problem/7576

import sys
from collections import deque

M, N=map(int, sys.stdin.readline().split())
box=[list(map(int, input().split())) for _ in range(N)]

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
queue=deque()
ret=0


def BFS():
    while queue:
        x, y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and box[nx][ny]==0:
                queue.append([nx, ny])
                box[nx][ny]=box[x][y]+1


for n in range(N):
    for m in range(M):
        if box[n][m]==1:
            queue.append([n, m])

BFS()

for i in box:
    for j in i:
        if j==0:
            print(-1)
            exit(0)

    ret=max(ret, max(i))
print(ret-1)