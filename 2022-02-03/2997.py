a = list(map(int, input().split()))

a.sort()

t1 = a[1] - a[0]
t2 = a[2] - a[1]

if t1 == t2:
    print(a[2] + a[1] - a[0])
elif t1 < t2:
    print(a[1] + a[1] - a[0])
else:
    print(a[0] + a[2] - a[1])