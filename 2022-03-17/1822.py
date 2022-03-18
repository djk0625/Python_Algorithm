import sys


n, m = map(int, sys.stdin.readline().split())
a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))

answer = a - b

if answer:
    print(len(answer))
    list = sorted(answer)
    for i in list:
        print(i, end=' ')
else:
    print(0)