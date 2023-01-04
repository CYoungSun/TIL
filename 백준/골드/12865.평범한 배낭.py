N, K = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]
arr.sort(key=lambda x:x[0])
arr2 = [[[-1], 0] for _ in range((K+1))]
for i in range(len(arr)):
    for j in range(1, K+1):
        if arr[i][0] <= j:
            if not (i in arr2[j][0]):
                if arr[i][1] > arr2[j][1]:
                    arr2[j][1] = arr[i][1]
                    arr2[j][0] = [i]
            if arr2[j][1] <= arr[i][1] + arr2[j-arr[i][0]][1]:
                if not(i in arr2[j-arr[i][0]][0]):
                    arr2[j][1] = arr[i][1] + arr2[j-arr[i][0]][1]
                    arr2[j][0] = list(arr2[j-arr[i][0]][0])
                    arr2[j][0].append(i)
                else:
                    arr2[j][1] = arr2[j-arr[i][0]][1]
                    arr2[j][0] = list(arr2[j-arr[i][0]][0])

print(arr2[K][1])