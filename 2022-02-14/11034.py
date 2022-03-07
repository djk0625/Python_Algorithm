while True:
    try:
        a, b, c = map(int, input().split())

        if b-a-1 > c-b-1:
            print(b-a-1)
        else:
            print(c-b-1)
    except:
        break