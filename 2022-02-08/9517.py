k = int(input())
n = int(input())

time = 210

for i in range(n):
    a, b = input().split()
    
    time -= int(a)
   
    if time <= 0:
        print(k)
        break
    
    if b == "T":
        k += 1
        if k > 8:
            k = 1
    elif b == "N" or b == "P":
        continue