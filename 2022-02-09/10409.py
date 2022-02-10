n, m = map(int, input().split())
t = list(map(int, input().split()))

answer = 0
for i in t:
    m -= i
    
    if m >= 0:
        answer += 1
    else:
        break
print(answer)