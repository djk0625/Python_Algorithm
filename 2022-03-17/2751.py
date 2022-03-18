import sys


n = int(sys.stdin.readline())
answer = []

for i in range(n):
    t = int(sys.stdin.readline())
    answer.append(t)

answer.sort()
    
for j in answer:
    print(j)