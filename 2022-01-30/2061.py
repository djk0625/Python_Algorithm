def checkPrime(n):
    sieve=[True]*n
    a=int(n ** 0.5)
    for i in range(2,a+1):
        if sieve[i]:
            for j in range(i+i,n,i):
                sieve[j]=False
    return [i for i in range(2,n) if sieve[i]==True]

K, L = map(int, input().split())
answer = 0

t = checkPrime(L)
for i in range(len(t)):
    if K % t[i] == 0:
        print("BAD", t[i])
        exit()
if answer == 0:
    print("GOOD")