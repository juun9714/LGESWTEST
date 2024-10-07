def DFS(n):
    visited[n]=True
    if visited[arr[n]]:
        return
    else:
        DFS(arr[n])

T=(int)(input())
for _ in range(T):
    N=(int)(input())
    arr=[0]+list(map(int, (input().split())))
    visited=[False for _ in range(N+1)]
    cycleCnt=0

    for i in range(1, N+1):
        if not visited[arr[i]]:
            DFS(arr[i])
            cycleCnt+=1

    print(cycleCnt)


'''
<1>
if visited[n]:

과

if visited[n]==True:

의 결과가 다르다...

1번이 안전

<2>
처음에 DFS 시작할 때, visited[i]로 해도 됨...
visited[arr[i]]로 해도 됨....

방법 차이임
'''