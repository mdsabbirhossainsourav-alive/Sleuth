question = input().strip()
vowels = "AEIOUYaeiouy"
for ch in reversed(question[:-1]):
    if ch.isalpha():
        print("YES" if ch in vowels else "NO")
        break
