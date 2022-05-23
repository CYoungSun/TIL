import sys
input = sys.stdin.readline
N = int(input())
for tc in range(N):
    n = int(input())
    bucket = [0] * (n+1)
    bucket[0] = 0
    bucket[1] = 1
    if n >= 2:
        bucket[2] = 2
        if n >= 3:
            bucket[3] = 4
    for i in range(4, n+1):
        a, b, c = 0, 0, 0
        if i-1 >= 0:
            a = i-1
        if i-2 >= 0:
            b = i-2
        if i-3 >= 0:
            c = i-3
        bucket[i] = bucket[a] + bucket[b] + bucket[c]
    print(bucket[n])