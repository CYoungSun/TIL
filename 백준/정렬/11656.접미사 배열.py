import sys
input = sys.stdin.readline
s = input().strip()
arr = []
for i in range(len(s)):
    arr.append(s[i:])
arr.sort()
for j in range(len(s)):
    print(arr[j])