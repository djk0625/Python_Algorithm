N, m, M, T, R = map(int, input().split())
X = m
answer = e =  0

if m + T > M:
    print("-1")
else:
    while e < N:
        if X + T <= M:
            X += T
            answer += 1
            e += 1
        else:
            X = max(X - R, m)
            answer += 1
    print(answer)