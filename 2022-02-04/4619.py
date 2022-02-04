while True:
    b, n = map(int, input().split())
    
    if b == 0 and n == 0:
        break

    i = 0
    
    while i ** n < b:
        i += 1
    
    if i ** n - b < b - ((i - 1) ** n):
        print(i)
    else:
        print(i - 1)