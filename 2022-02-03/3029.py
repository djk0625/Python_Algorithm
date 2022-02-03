a1, b1, c1 = map(int, input().split(":"))
a2, b2, c2 = map(int, input().split(":"))

n = a1 * 3600 + b1 * 60 + c1
m = a2 * 3600 + b2 * 60 + c2

if n >= m:
    m += 3600 * 24
    
answer = m - n

answer1 = answer // 3600
answer2 = (answer % 3600) // 60
answer3 = (answer % 3600) % 60

print("%02d:%02d:%02d" %(answer1, answer2, answer3))