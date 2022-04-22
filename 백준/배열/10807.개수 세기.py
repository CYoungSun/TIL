N = int(input())
arr = list(map(int, input().split()))
n = int(input())
bucket = [0] * 201
for i in arr:
    bucket[i+100] += 1
print(bucket[n+100])