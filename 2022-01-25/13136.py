a, b, c = map(int, input().split())

if a % c == 0 and b % c == 0:
    n = a // c
    m = b // c
    print(n * m)
elif a % c != 0 and b % c == 0:
    n = (a // c) + 1
    m = b // c
    print(n * m)
elif a % c == 0 and b % c != 0:
    n = a // c
    m = (b // c) + 1
    print(n * m)
else:
    n = (a // c) + 1
    m = (b // c) + 1
    print(n * m)