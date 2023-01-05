N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dr = [[-1, 0], [0, 1], [1, 0], [0, -1]]
flag = 0

while 1:
    if arr[r][c] == 0:
        ans += 1
        arr[r][c] = 2
    newd = (d+3) % 4
    dy, dx = dr[newd]
    if 0 <= r+dy < N and 0 <= c+dx < M:
        if arr[r+dy][c+dx] == 0:
            r += dy
            c += dx
            d = newd
            flag = 0
            continue
        else:
            if flag == 4:
                dy, dx = dr[(d+2) % 4]
                if 0 <= r+dy < N and 0 <= c+dx < M:
                    if arr[r+dy][c+dx] != 1:
                        r += dy
                        c += dx
                        flag = 0
                        continue
                    else:
                        break
                else:
                    break
            else:
                flag += 1
                d = newd
            continue
print(ans)