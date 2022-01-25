a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if e > c:
    n = b + ((e - c) * d)
else:
    n = b
    
if a * e < n:
    print(a * e)
else:
    print(n)