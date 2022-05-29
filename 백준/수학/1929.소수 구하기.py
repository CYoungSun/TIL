import sys
input = sys.stdin.readline
M, N = map(int, input().split())
check=[0]*(1000001)
answer = []
ans = 0
for i in range(2, N+1):
    if check[i] == 0: answer.append(i)
    for j in range(i+i,N+1,i):
        check[j]=1
for j in answer:
    if M <= j <= N:
        print(j)