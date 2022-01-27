a, b, c = map(int, input().split())

fa = b
fb = a - b
ra = c
rb = a - c

print(min(fa, ra) + min(fb, rb))