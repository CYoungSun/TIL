import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
visit[0][0] = 1
q = deque()
q.append([0, 0, 1])
ans = 0
while q:
    y, x, cnt = q.popleft()
    if y == N-1 and x == M-1:
        ans = cnt
        break
    directy = [0, 1, 0, -1]
    directx = [1, 0, -1, 0]
    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]
        if 0 <= dy < N and 0 <= dx < M:
            if visit[dy][dx] == 1:
                continue
            if arr[dy][dx] == 0:
                continue
            visit[dy][dx] = 1
            q.append([dy, dx, cnt+1])
print(ans)