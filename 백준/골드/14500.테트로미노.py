import sys
input = sys.stdin.readline

def dfs(level, SUM, y, x):
    global ans
    if level == 4:
        if SUM >= ans:
            ans = SUM
        return
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if visit[ny][nx] == 1:
                continue
            visit[ny][nx] = 1
            dfs(level+1, SUM+MAP[ny][nx], ny, nx)
            visit[ny][nx] = 0

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
ans = -1
move = [
    [[-1, 0], [1, 0], [0, 1]],
    [[0, -1], [0, 1], [1, 0]],
    [[0, -1], [0, 1], [-1, 0]],
    [[-1, 0], [1, 0], [0, -1]]
]
for i in range(N):
    for j in range(M):
        dfs(0, 0, i, j)
        for k in range(4):
            SUM = MAP[i][j]
            for l in range(3):
                ny = i + move[k][l][0]
                nx = j + move[k][l][1]
                if 0 <= ny < N and 0 <= nx < M:
                    SUM += MAP[ny][nx]
            if SUM >= ans:
                ans = SUM
print(ans)