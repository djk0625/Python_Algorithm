A = list(map(int, input().split()))
B = list(map(int, input().split()))

n = 0
m = 0

result = "D"

for i in range(10):
    if A[i] > B[i]:
        n += 3
        result = "A"
    elif A[i] < B[i]:
        m += 3
        result = "B"
    else:
        n += 1
        m += 1
    
    if n > m:
        result = "A"
    elif n < m:
        result = "B"
    else:
        if result == "A":
            result = "A"
        elif result == "B":
            result = "B"
        else:
            result = "D"

print(n, m)
print(result)