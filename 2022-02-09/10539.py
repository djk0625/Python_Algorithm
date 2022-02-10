n = int(input())
m = list(map(int, input().split()))

answer = []
answer.append(m[0])

for i in range(1, n):
    answer.append((m[i] * (i+1)) - sum(answer))

for i in answer:
    print(i, end=' ')