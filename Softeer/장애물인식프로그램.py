import sys
from collections import deque

input=sys.stdin.read
data=input().splitlines()
N=int(data[0])

field=[]

for i in range(1, N+1):
    field.append(list(map(int, list(data[i])))) # 조심심

visited=[[0 for _ in range(N)] for _ in range(N)]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

def BFS(x, y):
    queue=deque()
    queue.append((x, y))
    visited[x][y]=1
    cnt=1
    
    while queue:
        tx, ty = queue.popleft()
        
        for i in range(4):
            nx=tx+dx[i]
            ny=ty+dy[i]
            
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue

            if visited[nx][ny]==0 and field[nx][ny]==1:
                queue.append((nx, ny))
                visited[nx][ny]=1
                cnt+=1

    return cnt

group=[]

for i in range(N):
    for j in range(N):
        if visited[i][j]==0 and field[i][j]==1:
            group.append(BFS(i,j))

print(len(group))
group.sort() # 오름차순으로 출력하는 조건!!
for g in group:
    print(g)