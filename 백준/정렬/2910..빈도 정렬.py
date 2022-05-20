import sys
input = sys.stdin.readline
N, C = map(int, input().split())
arr = list(map(int, input().split()))
dic = {}
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
dic = sorted(dic.items(), key=lambda x:-x[1])
ans = []
for j in range(len(dic)):
    for k in range(dic[j][1]):
        ans.append(dic[j][0])
print(*ans)