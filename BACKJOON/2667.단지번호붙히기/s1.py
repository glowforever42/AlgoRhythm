# 좌우 혹은 위아래로 붙어있는집이 있어야한다

import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(input()) # 지도의 크기 
graph = [list(map(int, input())) for _ in range(T)]

print(graph)


# print(arr)