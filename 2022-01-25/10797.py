n = int(input())
car = list(map(int, input().split()))

count = 0

for i in range(len(car)):
    if car[i] == n:
        count += 1
        
print(count)