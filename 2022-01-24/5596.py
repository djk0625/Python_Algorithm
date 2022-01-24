a, b, c, d = map(int, input().split())
o, p, q, r = map(int, input().split())

sum = a + b + c + d
sum2 = o + p + q + r

if sum > sum2:
    print(sum)
elif sum == sum2:
    print(sum)
else:
    print(sum2)