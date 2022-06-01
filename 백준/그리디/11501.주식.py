import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    n = 0
    ans = 0
    for i in range(N-1, -1, -1):
        if i == N-1:
            n = arr[i]
        if arr[i] < n:
            ans += n - arr[i]
        elif arr[i] > n:
            n = arr[i]
    print(ans)
