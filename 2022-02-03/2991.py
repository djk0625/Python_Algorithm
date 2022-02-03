a, b, c, d = map(int, input().split())
people = list(map(int, input().split()))

for i in people:
    answer = 0
    
    if 0 < i % (a+b) <= a:
        answer += 1
    
    if 0 < i % (c+d) <= c:
        answer += 1

    print(answer)