from sys import stdin


n = int(stdin.readline())

c = d = 0

for i in range(n):
    a, b = map(int, stdin.readline().split())
    
    if a > b:
        c += 1
    elif a < b:
        d += 1
        
print(c, d)