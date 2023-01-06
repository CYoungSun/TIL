import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
arr = deque(map(int, input().split()))
robot = deque([0]*2*N)
ans = 1
count = 0
flag = 0
while 1:
    arr.rotate(1)
    robot.rotate(1)
    if robot[N-1] == 1:
        robot[N-1] = 0
    for i in range(N-2, -1, -1):
        if robot[i] == 1:
            if robot[i+1] == 0 and arr[i+1] >= 1:
                robot[i] = 0
                robot[i+1] = 1
                arr[i+1] -= 1
                if arr[i+1] == 0:
                    count += 1
                    if count >= K:
                        flag = 1
                        break
        if robot[N-1] == 1:
            robot[N-1] = 0
    if flag == 1:
        break
    if arr[0] > 0:
        robot[0] = 1
        arr[0] -= 1
        if arr[0] == 0:
            count += 1
            if count >= K:
                break
    ans += 1
print(ans)