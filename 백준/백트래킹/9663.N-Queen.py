import sys
from copy import deepcopy
input = sys.stdin.readline
def dfs(level):
    global cnt
    if level == N:
        cnt += 1
        return
    for i in range(N):
        flag = 0
        for j in range(level, -1, -1):
            if i == visit[j]:
                flag = 1
                break
            if level - j == abs(i-visit[j]):
                flag = 1
                break
        if flag == 1:
            continue
        visit[level] = i
        dfs(level+1)
        visit[level] = -1

N = int(input())
visit = [-1] * N
cnt = 0
dfs(0)
print(cnt)