
def checkTime(limit, diffs, times, level):
    sumTime=0
    for i in range(len(diffs)):
        if level>=diffs[i]:
            sumTime+=times[i]
        else:
            sumTime+= times[i]*(diffs[i]-level+1) + times[i-1]*(diffs[i]-level)

    if sumTime<=limit:
        return +1 # move to left (lower level)
    elif sumTime>limit: 
        return -1 # move to right (higher level)

def solution(diffs, times, limit):
    answer = 0
    start=min(diffs)
    end=max(diffs)
    
    
    while start<=end:
        mid=(end+start) // 2 # end-start가 아니라.. end+start임
        result=checkTime(limit, diffs, times, mid)
        if result == 1:
            end=mid-1 # end=mid가 아니라 end=mid-1임
            answer=mid # 정답의 포인트 
        else:
            start=mid+1 #start=mid가 아니라 start=mid+1임
       
    return answer


ex_diffs=[1, 5, 3]
ex_times=[2, 4, 7]
limit = 30

print(solution(ex_diffs, ex_times, limit))