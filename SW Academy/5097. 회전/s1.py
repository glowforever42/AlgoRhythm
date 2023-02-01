import sys
from collections import deque
sys.stdin = open('input.txt')

# N개의 숫자 중에 첫번째 숫자룰 맨뒤로 보내는 행위를 M번 반복함

T = int(input())

Q = deque()
result = 0
for tc in range(1, T+1):
    N, M = map(int,input().split())
    C = input().split()

    Q = deque(C)
    for j in range(M):
        P = Q.popleft()
        Q.append(P)
        result = Q[0]

    print('#{} {}'.format(tc, result))
    # if M >= 1:

