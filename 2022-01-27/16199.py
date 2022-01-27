a, b, c = map(int, input().split())
d, e, f = map(int, input().split())

n = 0
m = d - a + 1
t = d - a

if d > a:
    if e > b or (b == e and f >= c):
        n = d - a
    else:
        n = d - a - 1

print(n)
print(m)
print(t)