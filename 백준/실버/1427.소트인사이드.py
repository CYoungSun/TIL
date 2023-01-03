N = [*map(int, input())]
N.sort(reverse=True)
for _ in range(len(N)):
    print(N[_], end="")