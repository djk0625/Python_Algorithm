n = int(input())

answer = 5
plus = 7
if n == 1:
    print(answer)

else:
    for i in range(1, n):
        answer += plus
        plus += 3
        
    print(answer % 45678)