a, b, c = map(int, input().split())
answer = [0] * 81

for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            answer[i+j+k] += 1
print(answer.index(max(answer)))