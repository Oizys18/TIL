# SWEA 1989 Palindrome

for t in range(int(input())):
    word = input()
    print(f"#{t+1} {1 if word == word[::-1] else 0}")
