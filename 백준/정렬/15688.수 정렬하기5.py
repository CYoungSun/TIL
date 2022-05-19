import sys
input = sys.stdin.readline
N = int(input())
dic = {}
for i in range(N):
    n = int(input())
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1
dic = sorted(dic.items(), key=lambda x:x[0])
for i in range(len(dic)):
    for j in range(dic[i][1]):
        print(dic[i][0])