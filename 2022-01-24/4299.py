n, m = map(int, input().split())

if n - m < 0 or (n - m) % 2 != 0:
    print("-1")
else:
    a = (n + m) // 2
    print(a, n -a)