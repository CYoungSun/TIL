def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    if n==m:
        print(int(factorial(m) / (factorial(1) * factorial(n))))
    else:
        print(int(factorial(m)/(factorial(m-n)*factorial(n))))