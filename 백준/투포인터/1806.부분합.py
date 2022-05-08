N, S = map(int, input().split())
numList = list(map(int, input().split()))

result = 987654321
right = 0
tempSum = 0
for left in range(N):

    while tempSum < S and right < N:
        tempSum += numList[right]
        right += 1

    if tempSum >= S:
        result = min(result, right - left)

    tempSum -= numList[left]

if result == 987654321:
    print(0)
else:
    print(result)