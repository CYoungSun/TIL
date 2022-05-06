import sys
input = sys.stdin.readline
N = int(input())
arr = [input().split() for _ in range(N)]
for i in range(N):
    arr[i][0] = int(arr[i][0])
arr.sort(key=lambda x:x[0])
for j in range(N):
    print(*arr[j])