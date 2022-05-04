import sys
input = sys.stdin.readline
N = int(input())
arr = [0] * 10001
for i in range(N):
    n = int(input())
    arr[n] += 1
for j in range(len(arr)):
    if arr[j] != 0:
        for k in range(arr[j]):
            print(j)