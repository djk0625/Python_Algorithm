n = int(input())
t = list(input())
    
a = 0
b = 0

for i in range(0, len(t)):
    if t[i] == "A":
        a += 1
    elif t[i] == "B":
        b += 1

if a > b:
    print("A")
elif a < b:
    print("B")
elif a == b:
    print("Tie")