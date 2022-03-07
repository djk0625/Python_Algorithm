while True:
    n = input()
    
    if n == "#":
        break

    answer = 0
    
    for i in n:
        if i in "aeiouAEIOU":
            answer += 1
            
    print(answer)