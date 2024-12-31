def solution(mats, park):
    answer = -1
    
    for a in range(len(park)):
        for b in range(len(park[0])):
            if park[a][b] != "-1":
                continue
            
            for mat in mats:
                Flag = True
                for i in range(a, a+mat):
                    for j in range(b, b+mat):
                        if i>=len(park) or j >= len(park[0]):
                            Flag=False
                            continue

                        if(park[i][j]!="-1"):
                            Flag=False

                if Flag == True:
                    answer=max(mat, answer)
    #max(ret)을 하면 돗자리를 못까는 경우에 대해서 -1을 반환하는 로직이 동작하지 않음 
    return answer