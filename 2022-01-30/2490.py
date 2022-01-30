answer = 0

for i in range(3):
    a, b, c, d = map(int, input().split())
    sum = a + b + c + d
    
    if sum == 0:
        answer = "D"
    elif sum == 1:
        answer = "C"
    elif sum == 2:
        answer = "B"
    elif sum == 3:
        answer = "A"
    else:
        answer = "E"
        
    print(answer)
        
