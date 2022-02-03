t = int(input())

for _ in range(t):
    n = int(input())
    answer = 0
    
    while n > 0:
        if n % 2 == 1:
            print(answer, end = ' ')
        n = n // 2
        answer += 1