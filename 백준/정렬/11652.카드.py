import sys
input = sys.stdin.readline
N = int(input())
bucket = {}
ans = 0
num = 0
for i in range(N):
    n = int(input())
    if n in bucket:
        bucket[n] += 1
    else:
        bucket[n] = 1
bucket = sorted(bucket.items(), key=lambda x:(-x[1], x[0]))
print(bucket[0][0])