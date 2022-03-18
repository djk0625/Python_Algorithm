import sys


n, m = map(int, sys.stdin.readline().split())

a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))

c = a - b
d = b - a

list1 = sorted(c)
list2 = sorted(d)

print(len(list1) + len(list2))