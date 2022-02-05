list = []

for i in range(10):
    n = int(input())
    list.append(n)
    
    answer = sum(list) - list[0]

print(list[0] - answer)