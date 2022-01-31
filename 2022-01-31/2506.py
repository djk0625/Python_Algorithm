N = int(input())
test = list(map(int, input().split()))

answer = 0
score = 0

for i in  range(N):
    if test[i] == 1:
        score += 1
        answer += score
    else:
        score = 0

print(answer)