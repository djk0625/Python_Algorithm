while True:
    a = input()
    
    if a == "0":
        break
    
    t = len(a)
    answer = "yes"
    for i in range(t // 2):
        if a[i] != a[t-1-i]:
            answer ="no"
    
    print(answer)