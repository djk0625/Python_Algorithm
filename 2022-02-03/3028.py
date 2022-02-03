t = [1, 0, 0]
a = input()

for i in a:
    if i == 'A':
        t[0], t[1] = t[1], t[0]
    elif i == 'B':
        t[1], t[2] = t[2], t[1]
    else:
        t[0], t[2] = t[2], t[0]
print(t.index(1) + 1)