n = int(input())
list = [350.34, 230.90, 190.55, 125.30, 180.90]

for i in range(n):
    a, b, c, d, e = map(int, input().split())
    
    answer = (a * list[0]) + (b * list[1]) + (c * list[2]) + (d * list[3]) + (e * list[4])
    
    print("$" + "%.2f" % answer) 