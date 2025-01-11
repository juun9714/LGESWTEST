import sys

n=int(input())
halves=list(map(int, input().split()))
halves.sort()
tan=2
max_num=0

while tan<=max(halves):
    tmp_num=0
    for h in halves:
        if h%tan==0:
            tmp_num+=1

    if tmp_num>max_num:
        max_num=tmp_num

    tan+=1

print(max_num)
