a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = []

for i in range(4):
    t = a[i] - b[i]
    answer.append(t)
    
if sum(answer) > 0:
    print("Gunnar")
elif sum(answer) < 0:
    print("Emma")
else:
    print("Tie")