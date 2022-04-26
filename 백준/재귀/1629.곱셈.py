A, B, C = map(int, input().split())


def func(a, b, c):
    if b == 1:
        return a % c
    elif b == 2:
        return (a * a) % c

    else:
        if b % 2:
            return ((func(a, b // 2, c) ** 2) * a) % c

        else:
            return ((func(a, b // 2, c) ** 2)) % c


print(func(A, B, C))