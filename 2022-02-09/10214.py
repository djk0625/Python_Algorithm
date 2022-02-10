t = int(input())

for _ in range(t):
    
    n = 0
    m = 0
    
    for i in range(9):
        a, b = map(int, input().split())
    
        n += a
        m += b
    
    if n > m:
        print("Yonsei")
    elif n < m:
        print("Korea")
    elif n == m:
        print("Draw")