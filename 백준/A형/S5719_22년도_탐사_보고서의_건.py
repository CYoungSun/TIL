from collections import deque
T = int(input())
for tc in range(1, T+1):
    F, N = map(int, input().split())
    arr = list(map(int, input().split()))
    n = len(arr)
    arr = deque(arr)
    cnt = 0
    cnt_turn = 0
    flag = -1
    dic = {}
    for i in range(n):
        if arr[i] in dic:
            dic[arr[i]] += 1
        else:
            dic[arr[i]] = 1
    max_num = sorted(dic.items(), key=lambda x:x[1], reverse=True)[0][0]
    while cnt != F-1:
        if cnt_turn % n == 0:
            flag = 0
            cnt_turn = 0
            n = len(arr)
        if dic[arr[0]] == dic[max_num]:
            if flag == 0:
                flag = 1
                dic[arr[0]] -= 1
                sorted_arr = sorted(dic.items(), key=lambda x:x[1], reverse=True)
                max_num = sorted_arr[0][0]
                for j in range(1, len(sorted_arr)):
                    if sorted_arr[j][1] == 0:
                        continue
                    else:
                        break
                else:
                    arr.popleft()
                    break
                arr.popleft()
            else:
                arr.append(arr.popleft())
        else:
            arr.append(arr.popleft())
        cnt += 1
        cnt_turn += 1
    print(f'#{tc} {arr[0]}')

