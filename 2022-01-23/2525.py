a, b = map(int, input().split())
c = int(input())

a += c // 60
b += c % 60

if b >= 60:
    a = a+ 1
    b = b - 60

if a >= 24:
    a = a - 24
    
print(a, b)