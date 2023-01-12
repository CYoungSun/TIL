import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
apple = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
direction = [list(input().split()) for _ in range(L)]
arr = [[0] * N for _ in range(N)]
arr[0][0] = 1
turn = 1
head = [0, 0]
tail = deque([[0, 0]])
d = 0
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
while 1:
    y, x = head
    ny, nx = y + dy[d], x + dx[d]
    if 0 <= ny < N and 0 <= nx < N:
        if arr[ny][nx] == 1:
            break
        arr[ny][nx] = 1
        tail.append([ny, nx])
        head = [ny, nx]
    else:
        break
    for i in range(len(apple)):
        if ny == apple[i][0] - 1 and nx == apple[i][1] - 1:
            apple.pop(i)
            break
    else:
        if len(tail) > 1:
            tailY, tailX = tail.popleft()
            arr[tailY][tailX] = 0

    for j in range(len(direction)):
        if turn == int(direction[j][0]):
            if direction[j][1] == 'D':
                d = (d+1) % 4
            else:
                d = (d+3) % 4
    turn += 1
print(turn)