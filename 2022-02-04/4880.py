while True:
    a, b, c = map(int, input().split())
    
    if a == b == c == 0:
        break
    
    if b - a == c - b:
        print("AP", b - a + c)
    else:
        print("GP", (b // a) * c)