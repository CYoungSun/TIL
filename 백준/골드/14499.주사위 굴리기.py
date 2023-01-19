import sys
input = sys.stdin.readline
from collections import deque

N, M, x, y, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
move = deque(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]
while move:
    d = move.popleft()
    dy = [0, 0, 0, -1, 1]
    dx = [0, 1, -1, 0, 0]
    ny = y + dx[d]
    nx = x + dy[d]
    if 0 <= nx < N and 0 <= ny < M:
        y = ny
        x = nx
        if d == 1:
            dice[0], dice[2], dice[1], dice[5] = dice[1], dice[0], dice[5], dice[2]
        elif d == 2:
            dice[0], dice[1], dice[2], dice[5] = dice[2], dice[0], dice[5], dice[1]
        elif d == 3:
            dice[0], dice[4], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[4]
        else:
            dice[0], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[3]
        if MAP[nx][ny] == 0:
            MAP[nx][ny] = dice[0]
        else:
            dice[0] = MAP[nx][ny]
            MAP[nx][ny] = 0
        print(dice[5])
    else:
        continue