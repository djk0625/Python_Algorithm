a, b, c, d = map(int, input().split())

if a % b == 0:
    print((a-1) // b * c * d)
else:
    print(a // b * c * d)