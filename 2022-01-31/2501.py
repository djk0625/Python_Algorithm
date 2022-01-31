number = []

a, b = map(int, input().split())

for i in range(1, a+1):
    if a % i == 0:
        number.append(i)

number.sort()

if b > len(number):
    print("0")
else:
    print(number[b-1])