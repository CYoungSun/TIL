import sys
input = sys.stdin.readline
arr = []
for _ in range(int(input())):
    cnt = 0
    snum = input().rstrip()
    for i in snum:
        if i.isdigit():
            cnt += int(i)
    arr.append((snum, cnt))
arr.sort(key = lambda x: (len(x[0]), x[1], x[0]))
for i in arr:
    print(i[0])