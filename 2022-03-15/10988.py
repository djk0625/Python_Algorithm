n = input()

is_Palindrome = True

for i in range(len(n) // 2):
    if n[i] == n[-1-i]:
        is_Palindrome
    else:
        is_Palindrome = False

if is_Palindrome:
    print("1")
else:
    print("0")