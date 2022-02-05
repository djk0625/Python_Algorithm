n = int(input())

for _ in range(n):
    a = int(input())
    
    if a < 3:
        for i in range(a):
            print("#" * a)
        print()
    else:
        print("#" * a)
        for i in range(a - 2):
            print("#" + "J" * (a - 2) + "#")
        print("#" * a)
        print()