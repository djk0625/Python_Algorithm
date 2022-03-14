import sys


n = int(sys.stdin.readline())
sum = 0
answer = 0

for i in range(n):
    sum += i
    
    if sum <= n:
        answer = i
    
print(answer)