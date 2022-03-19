def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
    
n = int(input())
for _ in range(n):
    t = list(map(int, input().split()))
    t.sort(reverse=True)
    answer = [1]

    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            answer.append(gcd(t[i], t[j]))
            
    print(max(answer))