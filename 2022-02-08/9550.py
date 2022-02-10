t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
        
    answer = 0
    
    for i in a:
        answer += i // k
        
    print(answer)