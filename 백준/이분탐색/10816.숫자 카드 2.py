import sys
input = sys.stdin.readline
N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int ,input().split()))
cnt = [0] * 20000001
arr1.sort()
result = []
for i in arr1:
    cnt[i+10000000] += 1
for j in arr2:
    start = 0
    end = N-1
    while start<=end:
        middle = (start+end)//2
        if arr1[middle] > j:
            end = middle-1
        elif arr1[middle] < j:
            start = middle+1
        else:
            result.append(cnt[j+10000000])
            break
    else:
        result.append(0)
print(*result)