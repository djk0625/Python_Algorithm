answer = 0

for i in range(9):
    a = list(map(int, input().split()))
    
    if max(a) > answer:
        answer = max(a)
        x = i + 1
        y = a.index(answer) + 1
    
print(answer)
print(x, y)