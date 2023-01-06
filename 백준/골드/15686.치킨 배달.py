def dfs(level, k):
    global ans
    if level == M:
        score = 0
        for j in range(len(home)):
            hy, hx = home[j]
            d = 21e8
            for l in range(len(bucket)):
                by, bx = bucket[l]
                newD = abs(hy-by) + abs(hx-bx)
                if newD < d:
                    d = newD
            score += d
        if score <= ans:
            ans = score
        return
    for i in range(k, len(chic)):
        if used[i] == 1:
            continue
        used[i] = 1
        bucket.append(chic[i])
        dfs(level+1, i)
        used[i] = 0
        bucket.pop()


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
home = []
chic = []
bucket = []
ans = 21e8
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home.append([i, j])
        elif arr[i][j] == 2:
            chic.append([i, j])
used = [0] * len(chic)
dfs(0, 0)
print(ans)