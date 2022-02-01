answer = []

X, Y = map(int, input().split())

first_min = X * 1000 / Y
answer.append(first_min)

N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    
    t = a * 1000 / b
    answer.append(t)
    
    result = min(answer)
    
print("%.2f" % result)