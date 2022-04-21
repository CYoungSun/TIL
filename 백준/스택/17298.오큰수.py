N = int(input())
arr = list(map(int, input().split()))
result = [-1] * N
stack = []
for i in range(1, N+1):
    while stack:
        if stack[-1][1] < arr[i-1]:
            result[stack[-1][0]-1] = arr[i-1]
            stack.pop()
        else:
            break
    stack.append([i, arr[i-1]])
print(*result)