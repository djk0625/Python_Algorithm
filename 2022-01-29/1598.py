a, b = map(int, input().split())
a -= 1
b -= 1

n = abs(a // 4 - b // 4)
m = abs(a % 4 - b % 4)

print(n + m)