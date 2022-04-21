import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
stack = []
answer = 0
HEIGHT = 0
CNT = 1
for h in arr:
    while stack and stack[-1][HEIGHT] < h:
        answer += stack.pop()[CNT]
    if not stack:
        stack.append((h, 1))
        continue
    if stack[-1][HEIGHT] == h:
        cnt = stack.pop()[CNT]
        answer += cnt
        if stack:
            answer += 1
        stack.append((h, cnt + 1))
    else:
        stack.append((h, 1))
        answer += 1
print(answer)
