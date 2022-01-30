n = int(input())
t = [1, 2, 3]

for i in range(n):
    A, B = map(int, input().split())
    a = t.index(A)
    b = t.index(B)
    t[a], t[b] = t[b], t[a]
    
print(t[0])