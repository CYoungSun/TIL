import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move = deque(list(map(int, input().split())) for _ in range(M)) # d, s
cloud = deque([[N-1, 0], [N-2, 0], [N-1, 1], [N-2, 1]])
waterBug = deque()
visited = [[0] * N for _ in range(N)]
ans = 0
while move:
    d, s = move.popleft()
    dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
    dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    no = []
    visited = [[0] * N for _ in range(N)]
    for i in range(len(cloud)):
        y, x = cloud.popleft()
        ny = y + dy[d] * s
        nx = x + dx[d] * s
        if ny < 0:
            ny = (N + ny) % N
        elif ny >= N:
            ny = ny % N
        if nx < 0:
            nx = (N + nx) % N
        elif nx >= N:
            nx = nx % N
        arr[ny][nx] += 1
        visited[ny][nx] = 1
        waterBug.append([ny, nx])
    by = [1, 1, -1, -1]
    bx = [1, -1, 1, -1]
    while waterBug:
        y, x = waterBug.popleft()
        num = 0
        for i in range(4):
            ny = y + by[i]
            nx = x + bx[i]
            if 0 <= ny < N and 0 <= nx < N:
               if arr[ny][nx] >= 1:
                   num += 1
        arr[y][x] += num
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                continue
            else:
                if arr[i][j] >= 2:
                    arr[i][j] -= 2
                    cloud.append([i, j])
for i in range(N):
    for j in range(N):
        ans += arr[i][j]
print(ans)