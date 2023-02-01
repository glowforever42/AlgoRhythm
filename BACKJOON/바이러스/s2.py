import sys
from collections import deque

sys.stdin = open('input.txt')
T = int(input()) # 컴퓨터의 개수
N = int(input()) # 연결선의 개수

graph = [[] for _ in range(T+1)] # 그래프 초기화

visited = [0] * T # 방문 표시용


for i in range(N): # 그래프 생성
    a, b = map(int,input().split())
    graph[a] += [b] # a와 b연결
    graph[b] += [a] # b와 a연결 (양방향)

visited[1] = 1 # 1번 컴퓨터 부터 시작하니까 1번 컴퓨터는 미리 방문처리

queue = deque([1]) # 첫번째 컴퓨터에 대해 큐를 만듦
while queue: # 큐 빌떄까지 수행
    c = queue.popleft()
    for j in graph[c]: # 그래프의 c번 컴퓨터에 대해서 돌림
        if visited[j] == 0: # 만약 방문 안했으면
            queue.append(j) # 큐에 추가해주고
            visited[j] = 1 # 방문 처리 해줌
print(visited)
# print(graph)

# print(N)