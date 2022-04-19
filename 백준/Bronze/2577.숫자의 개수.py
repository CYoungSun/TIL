A = int(input())
B = int(input())
C = int(input())
N = str(A * B * C)
bucket = [0] * 10
for i in N:
    bucket[int(i)] += 1
for j in range(10):
    print(bucket[j])