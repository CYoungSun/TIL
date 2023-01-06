from collections import deque
from sys import stdin
input = stdin.readline
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
bucket = [[0] * N for _ in range(N)]
n = 1
ans = 0
score = [[0, 0] for _ in range((N**2 + 1))]
while 1:
    n = 1
    flag = 0
    for i in range(N):
        for j in range(N):
            if bucket[i][j] == 0:
                q = deque()
                bucket[i][j] = n
                score[n][0] += arr[i][j]
                score[n][1] += 1
                q.append([i, j])
                while q:
                    y, x = q.popleft()
                    dy = [0, 1, 0, -1]
                    dx = [1, 0, -1, 0]
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if 0 <= ny < N and 0 <= nx < N:
                            if bucket[ny][nx] != 0:
                                continue
                            if L <= abs(arr[ny][nx] - arr[y][x]) <= R:
                                flag = 1
                                q.append([ny, nx])
                                bucket[ny][nx] = n
                                score[n][0] += arr[ny][nx]
                                score[n][1] += 1
            n += 1
    if flag == 0:
        break
    for ni in range(N):
        for nj in range(N):
            index = bucket[ni][nj]
            arr[ni][nj] = score[index][0]//score[index][1]
    ans += 1
    bucket = [[0] * N for _ in range(N)]
    score = [[0, 0] for _ in range((N**2 + 1))]
print(ans)
