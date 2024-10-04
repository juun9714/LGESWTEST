import sys
from collections import deque

N = (int)(sys.stdin.readline())
aptComplex=[list(map(int, input())) for _ in range(N)]
visited=[[0 for _ in range(N)] for _ in range(N)]
dongCnt=[]


dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def BFS(x, y):
    queue=deque()
    queue.append((x, y))
    visited[x][y]=1
    cnt=1

    while queue:
        tx, ty=queue.popleft()
        for i in range(4):
            nx=tx+dx[i]
            ny=ty+dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue

            if aptComplex[nx][ny]==1 and visited[nx][ny]==0:
                queue.append((nx, ny))
                visited[nx][ny]=1
                cnt+=1

    # after finished BFS searching
    return cnt


for a in range(N):
    for b in range(N):
        if aptComplex[a][b]==1 and visited[a][b]==0:
            dongCnt.append(BFS(a,b))

print(len(dongCnt))
for cnt in sorted(dongCnt):
    print(cnt)