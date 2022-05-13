import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1],x[0]))
ans = []
for i in range(N):
    if len(ans) == 0:
        ans.append(arr[i][1])
    else:
        if arr[i][0] >= ans[-1]:
            ans.append(arr[i][1])
print(len(ans))