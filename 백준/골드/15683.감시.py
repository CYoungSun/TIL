from copy import deepcopy
import sys
input = sys.stdin.readline

def dfs(level, newArr):
    global ans
    if level == len(cctv):
        check = 0
        for i in range(N):
            for j in range(M):
              if newArr[i][j] == 0:
                  check += 1
        if check <= ans:
            ans = check
        return
    d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    y, x, typ = cctv[level]
    cctvType = []
    arr = deepcopy(newArr)
    if typ == 1:
        cctvType = cctv1
    elif typ == 2:
        cctvType = cctv2
    elif typ == 3:
        cctvType = cctv3
    elif typ == 4:
        cctvType = cctv4
    else:
        cctvType = cctv5
    for i in range(len(cctvType)):
        for j in range(len(cctvType[i])):
            n = 1
            while 1:
                ny = y + d[cctvType[i][j]][0] * n
                nx = x + d[cctvType[i][j]][1] * n
                if 0 > ny or 0 > nx or N <= ny or M <= nx:
                    break
                if arr[ny][nx] == 6:
                    break
                arr[ny][nx] = 1
                n += 1
        dfs(level+1, arr)
        arr = deepcopy(newArr)




N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cctv = []
ans = 21e8
cctv1 = [[0], [1], [2], [3]]
cctv2 = [[0, 1], [2, 3]]
cctv3 = [[0, 2], [0, 3], [1, 2], [1, 3]]
cctv4 = [[0, 1, 2], [0, 1, 3], [2, 3, 0], [2, 3, 1]]
cctv5 = [[0, 1, 2, 3]]
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and arr[i][j] != 6:
            cctv.append([i, j, arr[i][j]])

dfs(0, arr)
print(ans)