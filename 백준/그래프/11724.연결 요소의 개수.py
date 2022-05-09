import sys
input = sys.stdin.readline
def findboss(n):
    if bucket[n] == 0:
        return n
    res = findboss(bucket[n])
    bucket[n] = res
    return res

def union(a, b):
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return
    bucket[a] = fb
    bucket[fa] = fb


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
bucket = [0] * (N+1)
for a, b in arr:
    union(a,b)
cnt = 0
for i in range(1, N+1):
    if bucket[i] == 0:
        cnt += 1
print(cnt)