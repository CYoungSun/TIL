import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
a = 0
b = 1
result = 21e8
arr.sort()
while a < N and b < N:
    dif = arr[b] - arr[a]
    if dif < M:
        b += 1
    else:
        result = min(result, dif)
        a += 1
print(result)