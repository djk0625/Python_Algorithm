n = int(input())

first = []
second = []

for i in range(n):
    a, b = map(int, input().split())
    
    first.append(a)
    second.append(b)
    
c = max(first) - min(first)
d = max(second) - min(second)

print(c * d)