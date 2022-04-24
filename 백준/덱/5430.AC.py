from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  p = input()
  n = int(input())
  s = input().strip()
  reverse = 0
  if len(s)>2:
    s = s[1:-1]
    lst = list(map(str,s.split(',')))
  else:
    lst = []
  que = deque(lst)

  for i in p:
    if i=='R':
      if reverse==1:
        reverse = 0
        continue
      reverse = 1
    elif i =='D':
      if len(que)==0:
        print('error')
        break
      if reverse ==0:
        que.popleft()
      else:
        que.pop()
  else:
    if reverse ==0:
        que = list(que)
        a = ",".join(que)
        print('['+a+']')
    else:
        que.reverse()
        que = list(que)
        a = ",".join(que)
        print('['+a+']')