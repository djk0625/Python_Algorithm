n = int(input())
m = list(map(int, input().split()))
m.sort()

if len(m) == 1:
    print(m[0] * m[0])
else:
    print(max(m) * min(m))