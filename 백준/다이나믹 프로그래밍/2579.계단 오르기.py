import sys
input = sys.stdin.readline
N = int(input())
ML = [0] * 300
MS = [0] * 300
for i in range(N):
    ML[i] = int(input())
MS[0] = ML[0]
MS[1] = ML[1] + ML[0]
MS[2] = max(ML[2] + ML[0], ML[2] + ML[1])
for i in range(3, N):
    MS[i] = max(ML[i] + ML[i - 1] + MS[i - 3], ML[i] + MS[i - 2])

print(MS[N - 1])