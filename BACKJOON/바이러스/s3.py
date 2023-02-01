import sys

sys.stdin = open('input.txt')

T = int(input())
N = int(input())

graph = [[] for _ in range(T+1)]
visited = [0] * (T+1)


for i in range(N):
    a, b = map(int,input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(v):
    visited[v] = 1
    for j in graph[v]:
        if visited[j] == 0:
            visited[j] = 1
            dfs(j)
dfs(1)
print(sum(visited)-1)