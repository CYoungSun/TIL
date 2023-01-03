def dfs(level):
    global cnt
    if path.count(1) > cnt:
        return
    if level == N:
        cnt_ans = 0
        for i in range(len(answer)):
            for j in range(N):
                if path[j] == 1:
                    if j in can[i]:
                        cnt_ans += 1
                        break
        if cnt_ans == len(answer):
            if cnt > path.count(1):
                cnt = path.count(1)
        return
    for i in range(2):
        path[level] = i
        dfs(level+1)
        path[level] = 0
while 1:
    try:
        N = int(input())
        answer = list(input())
        arr = [list(input()) for _ in range(N)]
        can = [[] for _ in range(len(answer))]
        for i in range(N):
            for j in range(len(arr[0])):
                if arr[i][j] == answer[j]:
                    can[j].append(i)
        path = [0] * N
        cnt = 21e8
        dfs(0)
        if cnt == 21e8:
            print(-1)
        else:
            print(cnt)
        blank = input()
    except Exception as e:
        break