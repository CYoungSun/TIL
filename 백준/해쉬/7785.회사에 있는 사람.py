import sys
input = sys.stdin.readline
N = int(input())
dict = {}
for i in range(N):
    name, action = input().split()
    if action == 'enter':
        dict[name] = 1
    else:
        del dict[name]
arr = dict.keys()
arr = sorted(arr, reverse=True)
for j in range(len(arr)):
    print(arr[j])