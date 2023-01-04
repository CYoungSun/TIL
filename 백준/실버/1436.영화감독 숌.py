N = int(input())

n = 1
a = '666'
arr = []
while n<=N:
    flag = 0
    for i in range(0,len(a)-2):
        if a[i] == '6':
            flag = 2
            if i+1 < len(a):
                if a[i+1] != '6':
                    flag = 1
            else:
                flag = 1
            if i+2 < len(a):
                if a[i+2] != '6':
                    flag = 1
            else:
                flag = 1
        if flag == 2:
            arr.append(a)
            n += 1
            break
    a = int(a)+1
    a = str(a)
if n == N + 1:
    print(arr[N-1])