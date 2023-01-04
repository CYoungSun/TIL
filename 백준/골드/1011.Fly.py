n = int(input())
for i in range(n):
    x, y =map(int, input().split())
    dis = y - x
    for i in range(100000):
        if(dis <= ((i+1)//2) * (i//2+1)):
            print(i)
            break