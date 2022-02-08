n = int(input())

answer = []
for i in range(n):
    a = int(input())
    t = list(map(int, input().split()))
    
    answer.append(sum(t))
    
    print(answer[i])