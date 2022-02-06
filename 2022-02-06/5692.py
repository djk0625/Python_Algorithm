from sys import stdin


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
while True:
    n = stdin.readline().rstrip()
    if int(n) == 0:
        break
    
    t = len(n)
    result = 0
    for i in range(t):
        result += int(n[i]) * factorial(t-i)
    print(result)