from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    queue = deque()
    visit = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                queue.append((i, j))
    count2 = 0
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            if arr[ny][nx] == 0 and visit[ny][nx] == 0:
                visit[ny][nx] = 1
                queue.append((ny, nx))
                count2 += 1

    global answer
    count = 0
    for i in range(N):
        count += arr[i].count(0)
    count -= count2
    answer = max(answer, count)


def makeWall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                cnt += 1
                makeWall(cnt)
                arr[i][j] = 0
                cnt -= 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


answer = 0
makeWall(0)
print(answer)