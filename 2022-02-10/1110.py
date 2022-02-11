n = int(input())
t = n
answer = 0

while True:
    a = n // 10
    b = n % 10
    c = (a + b) % 10
    n = (b * 10) + c
    
    answer += 1
    
    if t == n:
        break
print(answer)