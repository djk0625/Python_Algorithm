from sys import stdin


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a , a)

n = int(stdin.readline())
m = list(map(int, stdin.readline().split()))
t = gcd(m[0], gcd(m[1], m[-1]))

for i in range(1, (t // 2) + 1):
    if t % i == 0:
        print(i)
print(t)