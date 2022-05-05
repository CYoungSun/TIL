import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
for i in arr:
    print(i)