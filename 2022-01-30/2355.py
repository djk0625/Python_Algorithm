from sys import stdin


a, b = map(int, stdin.readline().split())

if a < b:
    n = a * (a - 1) // 2
    m = b * (b + 1) // 2
    print(m - n)
else:
    n = a * (a + 1) // 2
    m = b * (b - 1) // 2
    print(n - m)