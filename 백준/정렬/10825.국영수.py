import sys
input = sys.stdin.readline
N = int(input())
arr = [list(input().split()) for _ in range(N)]
arr.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in range(N):
    print(arr[i][0])