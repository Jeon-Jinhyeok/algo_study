def main():
    t = int(input())
    d = [0] * 12

    d[1] = 1
    d[2] = 2
    d[3] = 4

    for i in range(4, 12):
        d[i] = d[i-3] + d[i-2] + d[i-1]

    for _ in range(t):
        n = int(input())
        print(d[n])

main()