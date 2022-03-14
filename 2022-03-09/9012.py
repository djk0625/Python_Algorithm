import sys

n = int(sys.stdin.readline())

for _ in range(n):
    t = input()
    stack = []
    answer = False
        
    for i in range(len(t)):
        if t[i] == "(":
            stack.append(t[i])
        elif t[i] == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")