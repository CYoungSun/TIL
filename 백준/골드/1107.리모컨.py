N = int(input())
M = int(input())
if M != 0:
    arr = [*map(int, input().split())]
else:
    arr = []
current = 100
ans = abs(N-100)
while current<=1000000:
    current = str(current)
    for i in range(len(current)):
        if not(int(current[i]) in arr):
            continue
        else:
            break
    else:
        cal = abs(N-int(current))
        if cal+len(current) <= ans:
            ans = cal + len(current)
    current = int(current) +1
current = 100
while current>=0:
    current = str(current)
    for i in range(len(current)):
        if not (int(current[i]) in arr):
            continue
        else:
            break
    else:
        cal = abs(N - int(current))
        if cal+len(current) <= ans:
            ans = cal + len(current)
    current = int(current) - 1
print(ans)