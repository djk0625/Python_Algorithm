a, b = map(int, input().split())

if a != 0 and b < 0:
    print(a // b + 1)
    print(a % b - b)
    
print(a // b)
print(a % b)