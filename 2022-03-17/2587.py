answer = []

for i in range(5):
    t = int(input())
    answer.append(t)
    answer.sort()
    
print(sum(answer) // 5)
print(answer[2])