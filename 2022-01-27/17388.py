a, b, c = map(int, input().split())

if a + b + c >= 100:
    print("OK")
else:
    t = min(a, b, c)
    if t == a:
        print("Soongsil")
    elif t == b:
        print("Korea")
    else:
        print("Hanyang")