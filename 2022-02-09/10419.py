t = int(input())

for i in range(t):
    d = int(input())
    n = 0
    
    while (n+1) + (n+1) ** 2 <= d:
        n += 1
    
    print(n)