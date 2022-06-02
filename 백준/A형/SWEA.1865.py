def dfs(level, res):
    global ans
    if res * 100 < ans:
        return
    if level == N:
        if res * 100 > ans:
            ans = res * 100
        return
    for i in range(N):
        if visit[i] == 1:
            continue
        visit[i] = 1
        dfs(level+1, res * arr[level][i] * 0.01)
        visit[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    if N == 16:
        arr.sort(key=lambda x:max(x))
    ans = 0
    visit = [0] * N
    dfs(0, 1)
    print(f"#{tc}", format(ans, ".6f"))