i = 1

while True:
    n = int(input())
    
    if n == 0:
        break
    
    n1 = 3 * n
    
    if n1 % 2 == 0:
        n2 = n1 // 2
    else:
        n2 = (n1 + 1) // 2
    
    n3 = 3 * n2
    n4 = n3 // 9
    
    if n1 % 2 == 0:
        n = 2 * n4
    else:
        n = 2 * n4 + 1
        
    if n1 % 2 != 0:
        print(f"{i}. odd {3 * (3 * n + 1) // 2 // 9}")
    else:
        print(f"{i}. even {3 * (3 * n) // 2 // 9} ")
        
    i += 1
