import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
sum_i = 0
cnt_i = 0
ans = 0
for i in range(N):
    if cnt_i == 0:
        cnt_i += 1
        sum_i = arr[i] * N
    else:
        if arr[i] * (N-i) > sum_i:
            sum_i = arr[i] * (N-i)
print(sum_i)