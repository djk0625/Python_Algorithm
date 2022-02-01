pi = 3.1415927
n= 1

while True:
    a, b, c = map(float, input().split())
    
    if b == 0:
        break
    
    dist = a / (5280 * 12) * pi * b
    mph = dist / c * 3600
    
    print("Trip #%d: %.2f %.2f" %(n, dist, mph))
    n += 1