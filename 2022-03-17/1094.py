n = int(input())

answer = [64, 32, 16, 8, 4, 2, 1]
count = 0

for i in range(len(answer)):
    if n >= answer[i]:
        count += 1
        n -= answer[i]
    
    if n == 0:
        break

print(count)