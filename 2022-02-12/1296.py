n = input()
t = int(input())
name = sorted([input() for i in range(t)])
percent = index = 0

for i in range(t):  
    L = n.count("L") + name[i].count("L")
    O = n.count("O") + name[i].count("O")
    V = n.count("V") + name[i].count("V")
    E = n.count("E") + name[i].count("E")
    p = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    
    if percent < p:
        percent = p
        index = i

print(name[index])