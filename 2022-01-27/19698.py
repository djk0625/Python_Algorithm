N, W, H, L = map(int, input().split())

answer = (W // L) * (H // L)

if N < answer:
    print(N)
else:
    print(answer)