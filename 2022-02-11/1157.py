n = input().upper()
t = list(set(n))

answer = []
for i in t:
    count = n.count
    answer.append(count(i))
    
if answer.count(max(answer)) > 1:
    print("?")
else:
    print(t[(answer.index(max(answer)))])