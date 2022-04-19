N = int(input())
arr = [list(input().split()) for _ in range(N)]
result = []
for i in range(N):
    if arr[i][0] == 'push':
        result.append(int(arr[i][1]))
    elif arr[i][0] == 'top':
        if len(result) != 0:
            print(result[-1])
        else:
            print(-1)
    elif arr[i][0] == 'size':
        print(len(result))
    elif arr[i][0] == 'empty':
        if len(result) == 0:
            print(1)
        else:
            print(0)
    elif arr[i][0] == 'pop':
        if len(result) == 0:
            print(-1)
        else:
            print(result.pop())
    
