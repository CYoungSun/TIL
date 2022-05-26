import sys
input = sys.stdin.readline
N = int(input())
dic = {}
for i in range(N):
    s = input().strip()
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

arr = list(dic.keys())
arr.sort()
arr.sort(key=lambda x:len(x))
for i in range(len(arr)):
    print(arr[i])
