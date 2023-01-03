N = int(input())
ans = 0
for _ in range(N):
    W = input()
    bucket = [0] * 26
    for i in range(len(W)):
        if bucket[ord(W[i])-ord('a')] == 0:
            bucket[ord(W[i])-ord('a')] = 1
        else:
            if W[i-1] != W[i]:
                break
    else:
        ans += 1
print(ans)