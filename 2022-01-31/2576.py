number = []
answer = []

for i in range(7):
    n = int(input())
    number.append(n)
    
    if number[i] % 2 != 0:
        answer.append(number[i])

if answer:
    print(sum(answer))
    print(min(answer))
    
else:
    print("-1")