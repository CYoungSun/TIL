N = int(input())
number = 1
result = []
stack = []
flag = 0
for i in range(N):
    n = int(input())
    if number <= n:
        while number != n+1:
            result.append('+')
            stack.append(number)
            number += 1
    if stack[-1] == n:
        result.append('-')
        stack.pop()
    else:
        print('NO')
        flag = 1
        break
if flag == 0:
    for i in range(len(result)):
        print(result[i])