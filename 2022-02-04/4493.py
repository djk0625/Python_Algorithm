t = int(input())

for _ in range(t):
    n = int(input())
    P1 = 0
    P2 = 0

    for i in range(n):
        a, b = input().split()
        
        if (a == 'R' and b == 'S') or (a == 'S' and b =='P') or (a == 'P' and b == 'R'):
            P1 += 1
        elif (a == 'S' and b == 'R') or (a == 'P' and b == 'S') or (a == 'R' and b == 'P'):
            P2 += 1
        elif (a == 'R' and b == 'R') or (a == 'S' and b == 'S') or (a == 'P' and b == 'P'):
            P1 += 1
            P2 += 1
            
    if P1 > P2:
        print("Player 1")
    elif P1 < P2:
        print("Player 2")    
    else:
        print("TIE")