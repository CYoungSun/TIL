E, S, M = map(int, input().split())

n = 1
while 1:
    a = n % 15 if n % 15 != 0 else 15
    b = n % 28 if n % 28 != 0 else 28
    c = n % 19 if n % 19 != 0 else 19
    if a == E:
        if b == S:
            if c == M:
                print(n)
                break
    n+=1
