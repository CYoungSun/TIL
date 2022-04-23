from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
arr = [list(input().split()) for _ in range(N)]
q = deque()
for i in range(N):
    if arr[i][0] == 'push':
        q.append(arr[i][1])
    elif arr[i][0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif arr[i][0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    elif arr[i][0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif arr[i][0] == 'size':
        print(len(q))
    elif arr[i][0] == 'empty':
        if q:
            print(0)
        else:
            print(1)

