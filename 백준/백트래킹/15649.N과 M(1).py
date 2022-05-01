import sys
input = sys.stdin.readline
def dfs(level):
    if level == M:
        print(*path)
    for i in range(N):
        if visit[i] == 1:
            continue
        visit[i] = 1
        path.append(i+1)
        dfs(level+1)
        path.pop()
        visit[i] = 0
N, M = map(int, input().split())
visit = [0] * N
path = []
dfs(0)