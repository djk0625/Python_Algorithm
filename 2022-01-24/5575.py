for i in range(3):
    a, b, c, d, e, f = map(int, input().split())
    time = (d * 3600 + e * 60 + f) - (a * 3600 + b * 60 + c)
    print(time // 3600, (time % 3600) // 60, (time % 3600) % 60)