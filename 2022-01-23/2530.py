a, b, c = map(int,input().split())
n = int(input())

c = c + n
b += c // 60
a += b // 60

c %= 60
b %= 60
a %= 24
print(a, b, c)