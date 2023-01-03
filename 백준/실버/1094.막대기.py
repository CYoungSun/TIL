N = int(input())
ans = 1
L = 64
while N!=L:
    if N < L:
        L = L//2

    else:
        ans += 1
        N -= L
        L // 2
print(ans)
