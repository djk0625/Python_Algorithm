n = int(input())


for i in range(n):
    m = int(input())
    count = []
    answer = []
    
    for j in range(m):
        a, b = map(float, input().split())
        
        count.append(a)
        answer.append(a*b)
    
    grade = sum(answer) / sum(count)
    print(int(sum(count)), '%.1f' % grade)