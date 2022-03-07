n = int(input())
m = list(map(int, input().split()))
t = int(input())
cnt = 0

for i in m:
    if i % t == 0:
        cnt += i // t
    else:
        cnt += i // t + 1

print(t * cnt)