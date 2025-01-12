#input().split()으로 풀었는데 시간 초과남
#input=sys.stdin.read
#data=input().splitlines()
#map(int, data[0].split()) 으로 처리해야 함

import sys
input=sys.stdin.read
data=input().splitlines()

W, N = map(int, data[0].split())
gems=[]

for i in range(1, N+1):
    gems.append(list(map(int, data[i].split())))

gems.sort(key=lambda x: -x[1])
bag=0
value=0

for gem in gems:
    if bag==W:
        break
    else:
        rest=W-bag
        if rest >= gem[0]: #가방에 보물 그대로 넣을 수 있는 경우
            bag+=gem[0] # bag에 무게 추가
            value+=gem[0]*gem[1] # value에 무게*가격 추가
        else: # 가방에 공간은 있으나, 전체를 넣을 수는 없는 경우
            bag+=rest # 남은 공간을 모두 채우고
            value+=rest*gem[1] # 남은 공간만큼 보석을 잘라서 넣은 가격 추가


print(value)