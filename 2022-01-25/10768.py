n = int(input())
m = int(input())

if n > 2:
    print("After")
else:
    if n == 2 and m == 18:
        print("Special")
    elif n == 2 and m >= 18:
        print("After")
    else:
        print("Before")