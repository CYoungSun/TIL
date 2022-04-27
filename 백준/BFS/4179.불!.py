from collections import deque
import sys
def bfs():
    while fire:
        y, x = fire.popleft()
        directy = [0, 1, 0, -1]
        directx = [1, 0, -1, 0]
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if 0 <= dy < R and 0 <= dx < C:
                if not f_visit[dy][dx] and arr[dy][dx] != '#':
                    f_visit[dy][dx] = f_visit[y][x] + 1
                    fire.append([dy, dx])

    while J:
        y, x = J.popleft()
        directy = [0, 1, 0, -1]
        directx = [1, 0, -1, 0]
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if 0 <= dy < R and 0 <= dx < C:
                if not j_visit[dy][dx] and arr[dy][dx] != '#':
                    if not f_visit[dy][dx] or f_visit[dy][dx] > j_visit[y][x] + 1:
                        j_visit[dy][dx] = j_visit[y][x] + 1
                        J.append([dy, dx])
            else:
                return j_visit[y][x] + 1
    return 'IMPOSSIBLE'
input = sys.stdin.readline
R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
J = deque()
fire = deque()
f_visit = [[0] * C for _ in range(R)]
j_visit = [[0] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'J':
            J.append([i, j])
        elif arr[i][j] == 'F':
            fire.append([i, j])
print(bfs())
