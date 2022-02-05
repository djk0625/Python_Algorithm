n = int(input())

while True:
    a = input()
    
    if a == "=":
        break
    
    b = int(input())

    if a == "+":
        n += b
    elif a == "-":
        n -= b
    elif a == "*":
        n *= b
    elif a == "/":
        n //= b
print(n)
        