import sys
input = sys.stdin.readline
N = int(input())
arr = [list(input().split()) for _ in range(N)]
for i in range(N):
    bucket1 = [0] * 26
    bucket2 = [0] * 26
    for j in range(len(arr[i][0])):
        bucket1[ord(arr[i][0][j])-ord('a')] += 1
    for k in range(len(arr[i][1])):
        bucket2[ord(arr[i][1][k])-ord('a')] += 1
    for l in range(26):
        if bucket1[l] != bucket2[l]:
            print('Impossible')
            break
    else:
        print('Possible')