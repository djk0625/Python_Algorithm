k = int(input())
n = int(input())

answer = 0

for i in range(n):
    a, b = input().split()
    
    if b == "T":
        if answer >= 21000:
            break
        else:
            answer += int(a)
            k += 1
    elif b == "N" or b == "P":
        answer += int(a)
        
if answer >= 210:
    print(k-1)