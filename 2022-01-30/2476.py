money = []
N = int(input())

answer = 0

for i in range(N):
    a, b, c = map(int, input().split())
    
    if a == b == c:
        answer = 10000 + a * 1000
        money.append(answer)
    elif a == b and a != c:
        answer = 1000 + a * 100
        money.append(answer)        
    elif a == c and a != b:
        answer = 1000 + a * 100
        money.append(answer)      
    elif b == c and b != a:
        answer = 1000 + b * 100
        money.append(answer) 
    else:
        answer = max(a, b, c) * 100
        money.append(answer)

print(max(money))