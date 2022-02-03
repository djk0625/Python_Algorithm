t = int(input())

for _ in range(t):
    answer = []
    a = list(map(int, input().split()))
    
    for i in a:
        if i % 2 == 0:
            answer.append(i)
    
    print(sum(answer), min(answer))