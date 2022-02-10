t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    
    f = 0
    m = 0
    
    if n % h == 0:
        f = h * 100
        m = n // h
    else:
        f = (n % h) * 100
        m = (n // h) + 1
    print(f + m) 