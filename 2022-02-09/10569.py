n = int(input())

answer = 0
for i in range(n):
    a, b = map(int, input().split())
    
    answer = 2 - a + b
    
    print(answer)