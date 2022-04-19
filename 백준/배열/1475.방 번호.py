n = input()
bucket = [0] * 10
for s in n:
    bucket[int(s)] += 1
max_number = 0
six_nine = bucket[6] + bucket[9]
if six_nine % 2 == 0:
    bucket[6] = six_nine // 2
    bucket[9] = 0
else:
    bucket[6] = six_nine // 2 + 1
    bucket[9] = 0
for i in range(10):
    if bucket[i] > max_number:
        max_number = bucket[i]
print(max_number)