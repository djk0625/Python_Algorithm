a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + (a * 1000))
elif a == b:
    print(1000 + (a * 100))
elif b == c:
    print(1000 + (b * 100))
elif a == c:
    print(1000 + (c * 100))
else:
    if a > b > c:
        print(100 * a)
    elif a > c > b:
        print(100 * a)
    elif b > a > c:
        print(100 * b)
    elif b > c > a:
        print(100 * b)
    else:
        print(100 * c)
        