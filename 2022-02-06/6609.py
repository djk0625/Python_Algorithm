from sys import stdin

for i in stdin:    
    m, p, l, e, s, r, n = map(int, i.split())

    for i in range(n):
        a = m
        m = p // s
        p = l // r
        l = a * e

    print(m)