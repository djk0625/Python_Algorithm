n = int(input())

for i in range(n):
    t = list(map(int, input().split()))
    t.sort()
    
    print(f"Case #{i+1}: ", end='')
    
    if t[2] >= t[0] + t[1]:
        print("invalid!")
    
    elif t[0] == t[1] == t[2]:
        print("equilateral")
    
    elif t[0] == t[1] or t[1] == t[2] or t[0] == t[2]:
        print("isosceles")
    
    else:
        print("scalene")