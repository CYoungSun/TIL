from collections import deque
N, M = map(int, input().split())
arr = list(map(int, input().split()))
q = deque()
ans = 0
flag = 0
for i in range(1, N+1):
    q.append(i)
for n in arr:
    flag = 0
    while flag == 0:
        target = q.index(n)
        if n == q[0]:
            q.popleft()
            flag = 1
        elif target < len(q)-target:
            q.append(q.popleft())
            ans += 1
        else:
            q.appendleft((q.pop()))
            ans += 1
print(ans)


