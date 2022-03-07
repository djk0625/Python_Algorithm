n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    
    t = b * 2 - a
    k = b - t

    print(t, k)