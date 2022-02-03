answer = []

for i in range(5):
    a, b, c, d = map(int, input().split())
    
    t = a + b + c + d
    answer.append(t)

print(answer.index(max(answer))+ 1, max(answer))