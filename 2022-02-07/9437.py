while True:
    t = list(map(int, input().split()))
    
    if t == [0]:
        break
    
    for i in range(t[0] // 4):
        n = [2*i + 1, 2*i + 2, t[0]-2*i - 1, t[0]-2*i]
        if t[1] in n:
            n.remove(t[1])
            print(n[0], n[1], n[2])
        