N = int(input())
arr = list(map(int, input().split()))
result = [0] * N
stack = []
for i in range(1, N+1):
    while stack:
        if stack[-1][1] > arr[i-1]:
            result[i-1] = stack[-1][0]
            break
        else:
            stack.pop()
    stack.append([i, arr[i-1]])
print(*result)