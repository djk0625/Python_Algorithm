n = int(input())
m = int(input())
start = m

for i in range(n):
    a, b = map(int, input().split())
    
    m += a - b
    
    if m < 0:
        print("0")
        break
    
    if start <= m:
        start = m

if m > 0:
    print(start)