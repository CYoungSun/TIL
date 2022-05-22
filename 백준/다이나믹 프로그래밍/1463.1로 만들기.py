import sys
input = sys.stdin.readline
N = int(input())
bucket = [0] * (N+1)
bucket[0] = 21e8
for i in range(2, N+1):
    a, b, c = 0, 0, 0
    if i % 3 == 0:
        a = i // 3
    if i % 2 == 0:
        b = i // 2
    c = i - 1
    bucket[i] = min(bucket[a], bucket[b], bucket[c]) + 1
print(bucket[N])