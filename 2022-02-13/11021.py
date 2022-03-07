n = int(input())

for i in range(n):    
    try:
        a, b = map(int, input().split())
        t = a + b
        
        print(f"Case #{i+1}:", t)
    except:
        break