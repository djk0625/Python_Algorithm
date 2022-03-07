n = int(input())

a = []
b = []
for i in range(n):
    t = input()
    
    if t == "1":
        a.append(t)
    elif t == "0":
        b.append(t)
    
if len(a) > len(b):
    print("Junhee is cute!")
elif len(a) < len(b):
    print("Junhee is not cute!")