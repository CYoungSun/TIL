import sys
input = sys.stdin.readline
def dfs(k, cnt):
    global ans
    if k == 0:
        if cnt < ans:
            ans = cnt
        return
    for i in range(N):
        if visit[i] == 1:
            continue
        visit[i] = 1
        dfs(k % arr[i], cnt + k//arr[i])
        visit[i] = 0


N, K = map(int, input().split())
arr = list(int(input()) for _ in range(N))
visit = [0] * N
ans = 21e8
dfs(K, 0)
print(ans)