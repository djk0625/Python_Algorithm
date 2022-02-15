n = int(input())
answer = 1
direction = 0

for i in range(n):
    a, b, c = map(int, input().split())
    answer = answer * b // a
    if c == 1:
        if direction == 1:
            direction = 0
        elif direction == 0:
            direction = 1
    else:
        direction
print(direction, answer)