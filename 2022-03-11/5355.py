import sys


n = int(sys.stdin.readline())

for i in range(n):
    t = list(sys.stdin.readline().split())
    
    result = float(t[0])
    
    for j in range(1, len(t)):
        if t[j] == "@":
            result *= 3
        elif t[j] == "%":
            result += 5
        elif t[j] == "#":
            result -= 7

    print("%.2f" %result)