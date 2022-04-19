N = int(input())
result = []
for n in range(N):
    a = int(input())
    if a == 0:
        result.pop()
    else:
        result.append(a)
if len(result) == 0:
    print(0)
else:
    print(sum(result))