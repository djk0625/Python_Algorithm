while True:
    a, b, c = map(int, input().split())
    
    if a == b == c == 0:
        break
    
    t = round((a/b - a/c) * 3600)
    h = t // 3600
    m = (t % 3600) // 60
    s = t % 60
    print("%d:%02d:%02d" % (h, m, s))