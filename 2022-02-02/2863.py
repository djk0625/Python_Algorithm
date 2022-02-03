a, b = map(int, input().split())
c, d = map(int, input().split())

answer = []

t1 = a / c + b / d
t2 = c / d + a / b
t3 = d / b + c / a
t4 = b / a + d / c

answer.append(t1)
answer.append(t2)
answer.append(t3)
answer.append(t4)

print(answer.index(max(answer)))
