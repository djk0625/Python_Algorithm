from sys import stdin


a = int(stdin.readline())

arr = [0] * 26
answer = ""

for _ in range(a):
    n = stdin.readline()
    arr[ord(n[0]) - 97] += 1

for i in range(26):
    if arr[i] >= 5:
        answer += chr(i + 97)

if answer:
    print(answer)
else:
    print("PREDAJA")