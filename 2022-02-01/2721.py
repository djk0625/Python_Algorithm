T = int(input())

for i in range(T):
    n = int(input())
    
    sum = 0
    a = 0
    
    for j in range(1, n+1):
        for k in range(1, j+2):
            a += k
        sum += j * a
        a = 0

    print(sum)