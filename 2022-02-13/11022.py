t = int(input())

for i in range(t):
    try:
        a, b = map(int, input().split())
        n = a + b
        print(f"Case #{i+1}:", a, "+", b, "=", n)
    except:
        break