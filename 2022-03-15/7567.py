n = input()
answer = 10

for i in range(1, len(n)):
    if n[i-1] == n[i]:
        answer += 5
    else:
        answer += 10
        
print(answer)