from sys import stdin


n = int(stdin.readline())

answer = 0
for i in range(n):
    a = int(stdin.readline())
    
    answer += a
    
print(answer - n + 1)