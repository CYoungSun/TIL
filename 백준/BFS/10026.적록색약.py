import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = [list(input()) for _ in range(N)]
vector = ((-1, 0), (1, 0), (0, 1), (0, -1))
visited = None



def validate(x, y, nowColor):
    return 0 <= x < N and 0 <= y < N and not visited[y][x] and arr[y][x] == nowColor


def bfs():
    global visited
    visited = [[False] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                deq = deque()
                nowColor = arr[i][j]
                deq.append((j, i, nowColor))
                visited[i][j] = True
                cnt += 1

                while deq:
                    x, y, nowColor = deq.popleft()
                    for vx, vy in vector:
                        nx, ny = (x + vx, y + vy)
                        if validate(nx, ny, nowColor):
                            visited[ny][nx] = True
                            deq.append((nx, ny, nowColor))
    return cnt


a1 = bfs()

for y in range(N):
    for x in range(N):
        if arr[y][x] == 'R':
            arr[y][x] = 'G'

a2 = bfs()

print(a1, a2)