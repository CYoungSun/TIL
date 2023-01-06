import sys
from collections import deque
input = sys.stdin.readline

def find(y, x, fav):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    score = 0
    like = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if MAP[ny][nx] == 0:
                score += 1
            if MAP[ny][nx] in fav:
                like += 1
    return [y, x, score, like]

def cal(y, x):
    global ans
    num = MAP[y][x]
    score = 0
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if MAP[ny][nx] in favList[num]:
                score += 1
    if score == 1:
        ans +=1
    elif score == 2:
        ans += 10
    elif score == 3:
        ans += 100
    elif score == 4:
        ans += 1000


N = int(input())
arr = deque(map(int, input().split()) for _ in range(N**2))
MAP = [[0] * N for _ in range(N)]
favList = [0] * (N**2 + 1)
can = []
ans = 0
while arr:
    num, one, two, three, four = arr.popleft()
    fav = [one, two, three, four]
    favList[num] = fav
    blank = 0
    can = []
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 0:
                can.append(find(i,j,fav))
    can.sort(key=lambda x:[-x[3], -x[2], x[0], x[1]])
    MAP[can[0][0]][can[0][1]] = num
for i in range(N):
    for j in range(N):
        cal(i, j)
print(ans)