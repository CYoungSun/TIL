import sys
input = sys.stdin.readline
N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr1.sort()
arr2.sort(reverse=True)
ans = 0
for i in range(N):
    ans += arr1[i] * arr2[i]
print(ans)