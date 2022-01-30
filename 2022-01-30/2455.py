people = []
start = 0

for i in range(4):
    a, b = map(int, input().split())
    
    start += b
    start -= a
    
    people.append(start)
    
print(max(people))