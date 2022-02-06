while True:
    n = input()
    
    if n == '0':
        break
    
    answer = 0
    
    while True:
        t = 0
        
        for i in n:
            t += int(i)
        if t < 10:
            answer = t
            break
        else:
            n = str(t)
    print(answer)