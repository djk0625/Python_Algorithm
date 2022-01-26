a, b, c = map(int, input().split())

n = a * b / c
m = a / b * c

if n > m:
    print(int(n))
else:
    print(int(m))