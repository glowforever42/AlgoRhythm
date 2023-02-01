import sys
from collections import deque
# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

# 예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

# 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

sys.stdin = open('input.txt')

T = int(input()) # 컴퓨터의 개수
N = int(input()) # 연결선의 개수

graph = [[] for i in range(T+1)] # 그래프 초기화

visited = [0] * (T+1) # 방문 표시용

for i in range(N): # 그래프 생성
    a, b = map(int, input().split())
    graph[a] += [b] # a에 b를 연결
    graph[b] += [a] # b에 a를 연결 -> 양방향

visited[1] = 1 # 1번부터 시작이니까 방문표시 미리 해주기

# queue = deque([1])

# while queue: # 큐가 빌때까지 순회
#     c = queue.popleft()
#     for j in graph[c]: # c번 컴퓨터와 연결 된 컴퓨터 찾는 과정
#         if visited[j] == 0: # 방문하지 않은 컴퓨터라면
#             queue.append(j) # 그 컴퓨터를 큐에 추가해주고
#             visited[j] == 1 # 방문처리를 해줌
#     print(queue)

Q=deque([1])
while Q:
    c=Q.popleft()
    for nx in graph[c]:
        if visited[nx]==0:
            Q.append(nx)
            visited[nx]=1
    print(Q)
    print(graph)
# print(sum(visited)-1)
