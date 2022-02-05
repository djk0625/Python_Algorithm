n = int(input())

for _ in range(n):
    a = int(input())
    print(f"Pairs for {a}:", end = ' ')
    
    for i in range(1, a // 2 + 1):
        if i != a - i:
            if i != 1:
                print(',', end = ' ')
            print(i, a-i, end='')
    print()