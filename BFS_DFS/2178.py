import sys
from collections import deque


N, M=map(int, sys.stdin.readline().split())
maze = [list(map(int, input())) for _ in range(N)]


def BFS(x, y):
    dx=[-1, 1, 0, 0]
    dy=[0, 0, -1, 1]
    # 좌, 우, 하, 상

    queue=deque()
    queue.append((x, y))

    while queue:
        x, y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue

            if maze[nx][ny]==0:
                continue

            if maze[nx][ny]==1:
                maze[nx][ny]=maze[x][y]+1
                queue.append((nx, ny))

    return maze[N-1][M-1]
    
print(BFS(0,0))