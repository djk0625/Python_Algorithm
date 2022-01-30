while 1:
    a = list(map(int, input().split()))
    
    if a[0] == 0:
        break
    
    answer = 1
    
    for i in range(a[0]):
        odd = a[2*i + 1]
        even = a[2*i +2]
        answer = answer * odd - even
    
    print(answer)
    