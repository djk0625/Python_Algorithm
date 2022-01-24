a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if b % d != 0:
    n = b // d + 1
    m = c // e + 1
else:
    n = b // d
    m = c // e

if n > m:
    print(a - n)
else:
    print(a - m)