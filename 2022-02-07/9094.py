from sys import stdin


t = int(stdin.readline())

for _ in range(t):
    n, m = map(int, stdin.readline().split())
    
    answer = 0
    for a in range(1, n+1):
        for b in range(a+1, n):
            if (a ** 2 + b ** 2 + m) % (a * b) == 0:
                answer += 1
    print(answer)