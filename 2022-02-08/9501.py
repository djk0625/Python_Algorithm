t = int(input())

answer = 0
for _ in range(t):
    a, b = map(int, input().split())
    
    for i in range(a):
        l, m, n = map(int, input().split())
        
        if l * m // n >= b:
           answer += 1
           
    print(answer)
    answer = 0