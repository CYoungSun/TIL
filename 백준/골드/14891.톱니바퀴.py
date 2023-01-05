import sys
from collections import deque

def check_right(start, dirs):
    if start > 4 or gears[start - 1][2] == gears[start][6]:
        return

    if gears[start - 1][2] != gears[start][6]:
        check_right(start + 1, -dirs)
        gears[start].rotate(dirs)


def check_left(start, dirs):
    if start < 1 or gears[start][2] == gears[start + 1][6]:
        return

    if gears[start + 1][6] != gears[start][2]:
        check_left(start - 1, -dirs)
        gears[start].rotate(dirs)


gears = {}
for i in range(1, 5):
    gears[i] = deque(list(map(int, list(sys.stdin.readline().replace("\n", "")))))
n = int(sys.stdin.readline())

for _ in range(n):
    num, dirs = map(int, sys.stdin.readline().split())

    check_right(num + 1, -dirs)
    check_left(num - 1, -dirs)
    gears[num].rotate(dirs)

result = 0
for i in range(4):
    result += (2 ** i) * gears[i + 1][0]
print(result)