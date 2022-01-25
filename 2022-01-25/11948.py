a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

n = a + b + c + d - min(a,b,c,d)
m = max(e, f)

print(n + m)