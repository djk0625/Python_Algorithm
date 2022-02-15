a, b = map(int, input().split())
t = list(map(int, input().split()))
n = len(t)
m = []

for i in range(n):
    if t[i] < b:
        m.append(t[i])

print(" ".join(map(str, m)))