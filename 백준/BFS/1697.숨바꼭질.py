import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
arr = [0] * 100001
q = deque()
q.append((N, 0))
while q:
    X, cnt = q.popleft()
    if X == K:
        print(cnt)
        break
    if 0<= X-1 <= 100000:
        if arr[X-1] == 0:
            arr[X-1] = cnt+1
            q.append((X-1, cnt+1))
        elif arr[X-1] > cnt+1:
            arr[X-1] = cnt+1
            q.append((X-1, cnt+1))
    if 0<= X+1 <= 100000:
        if arr[X+1] == 0:
            arr[X+1] = cnt+1
            q.append((X + 1, cnt + 1))
        elif arr[X+1] > cnt+1:
            arr[X+1] = cnt+1
            q.append((X + 1, cnt + 1))
    if 0<= X*2 <= 100000:
        if arr[X*2] == 0:
            arr[X*2] = cnt+1
            q.append((X * 2, cnt + 1))
        elif arr[X*2] > cnt+1:
            arr[X*2] = cnt+1
            q.append((X * 2, cnt + 1))
