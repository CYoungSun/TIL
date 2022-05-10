import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
find = list(map(int, input().split()))
arr.sort()
for i in find:
    start = 0
    end = N-1
    while start<=end:
        middle = (start+end) // 2
        if i == arr[middle]:
            print(1)
            break
        elif i < arr[middle]:
            end = middle-1
        else:
            start = middle+1
    else:
        print(0)