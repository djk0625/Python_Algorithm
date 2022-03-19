from collections import deque
import sys


n = int(sys.stdin.readline())
d = deque([])

for i in range(n):
    t = sys.stdin.readline().split()
    
    if t[0] == "push_back":
        d.append(t[1])
    
    elif t[0] == "push_front":
        d.appendleft(t[1])
    
    elif t[0] == "pop_front":
        if not d:
            print("-1")
        else:
            print(d.popleft())
    
    elif t[0] == "pop_back":
        if not d:
            print("-1")
        else:
            print(d.pop())
    
    elif t[0] == "size":
        print(len(d))
    
    elif t[0] == "empty":
        if not d:
            print("1")
        else:
            print("0")
    
    elif t[0] == "front":
        if not d:
            print("-1")
        else:
            print(d[0])
            
    elif t[0] == "back":
        if not d:
            print("-1")
        else:
            print(d[-1])