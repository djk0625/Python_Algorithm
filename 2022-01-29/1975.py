from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    result = 0
    for i in range(2, 1001):
        x = n
        while x:
            if x % i == 0:
                result += 1
                x //= i
            else:
                break
    print(result)