n = int(input())
data = []
students = [0] * n

for i in range(n):
    data.append(list(map(int, input().split())))
    students[i] = [0] * n

for i in range(5):
    for j in range(n):
        for k in range(j+1, n):
            if data[j][i] == data[k][i]:
                students[k][j] = 1
                students[j][k] = 1

answer = []
for s in students:
    answer.append(s.count(1))
    
print(answer.index(max(answer)) + 1)