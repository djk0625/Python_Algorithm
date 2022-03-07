a, b = map(str, input().split())

n = int(a, 2)
m = int(b, 2)

t = n + m

print(bin(t)[2:])