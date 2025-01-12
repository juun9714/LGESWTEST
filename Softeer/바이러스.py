'''
import sys

K, P, N = map(int, input().split())

print(K*pow(P, N) % (1000000007))
'''
# 위와 같이 작성하였으나, 시간 초과로 인해 모든 TC 통과 불가
# 계산 과정에서 시간을 줄여야 함
#   곱셈 한번 할 때마다, mod 로 나눠줌으로써 값의 크기를 줄여. 
# 아래와 같이 작성하니 TC 전부 통과입니다!

import sys

K, P, N = map(int, input().split())
mod_val=1000000007
for _ in range(N):
    K=K * P % mod_val

print(K)