a = int(input())
b = int(input())

a -= a % 100

while True:
    if a % b == 0:
        break
    a += 1
    
print("%02d" %(a % 100))