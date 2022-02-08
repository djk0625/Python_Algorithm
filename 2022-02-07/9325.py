num = int(input())

for _ in range(num):
    a = int(input())
    t = int(input())

    cnt = 0
 
    for i in range(t):
        n, m = map(int, input().split())
        cnt += n*m
        
    print(a + cnt)