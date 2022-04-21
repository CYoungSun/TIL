N = int(input())
arr = [int(input()) for _ in range(N)]
ans = 0
stack = []
for i in range(1, N+1):
    while stack:
        if stack[-1][1] > arr[i-1]:
            ans += len(stack)
            break
        else:
            stack.pop()
    stack.append([i, arr[i-1]])
print(ans)