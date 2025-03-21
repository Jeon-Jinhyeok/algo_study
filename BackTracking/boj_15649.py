from itertools import permutations

n, m = map(int, input().split())

data = [i for i in range(1, n+1)]
ary = list(permutations(data, m))

for each in ary:
    print(" ".join(map(str, each)))