n, m = map(int, input().split())
answer = []

for _ in range(n):
    answer.append(input())
    
row = 0
column = 0

for i in range(n):
    if "X" not in answer[i]:
        row += 1

for j in range(m):
    column_list = []
    for i in range(n):
        column_list.append(answer[i][j])
    if "X" not in column_list:
        column += 1

print(max(row, column))