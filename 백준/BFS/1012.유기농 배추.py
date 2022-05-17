import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    arr = [[0] * N for _ in range(M)]
    visit = [[0] * N for _ in range(M)]
    for _ in range(K):
        x, y= map(int, input().split())
        arr[y][x] = 1
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1:
                if visit[i][j] == 1:
                    continue
                visit[i][j] = 1
                q = deque()
                q.append((i, j))
                while q:
                    y, x = q.popleft()
                    directy = [0, 1, 0, -1]
                    directx = [1, 0, -1, 0]
                    for k in range(4):
                        dy = y + directy[k]
                        dx = x + directx[k]
                        if 0 <= dy < M and 0 <= dx < N:
                            if arr[dy][dx] == 0:
                                continue
                            if visit[dy][dx] == 1:
                                continue
                            visit[dy][dx] = 1
                            arr[dy][dx] = 0
                            q.append((dy, dx))
    ans = 0
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1:
                ans += 1
    print(ans)