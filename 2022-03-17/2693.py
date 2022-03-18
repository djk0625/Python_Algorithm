import sys


n = int(sys.stdin.readline())

for i in range(n):
    t = list(map(int, sys.stdin.readline().split()))
    t.sort(reverse=True)
    
    print(t[2])