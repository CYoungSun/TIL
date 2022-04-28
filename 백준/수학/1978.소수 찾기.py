import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
check=[0]*(1001)
answer = []
ans = 0
for i in range(2, 1001):
    if check[i] == 0: answer.append(i)
    for j in range(i+i,1001,i):
        check[j]=1
for k in arr:
    if k in answer:
        ans += 1
print(ans)