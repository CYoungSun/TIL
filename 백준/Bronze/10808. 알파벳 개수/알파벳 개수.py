S = input()
bucket = [0] * 26
for i in S:
    n = ord(i)-ord('a')
    bucket[n] += 1
print(*bucket)