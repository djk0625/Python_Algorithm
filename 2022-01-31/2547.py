T = int(input())

result = "YES"

for i in range(T):
    
    t = input()
    N = int(input())
    
    answer = 0

    for _ in range(N):
       a = int(input())
       answer += a
       
       if answer % N == 0:
           result = "YES"
       else:
           result = "NO"
           
    print(result)
           