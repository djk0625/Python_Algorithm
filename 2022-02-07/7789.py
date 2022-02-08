a, b = input().split()

a_root = int(int(a) ** 0.5)

n = int(b + a)
n_root = int(n ** 0.5)

prime = "Yes"

for i in range(2, a_root + 1):
    if int(a) % i == 0:
        prime = "No"
        
for i in range(2, n_root + 1):
    if n % i == 0:
        prime = "No"
        
print(prime)