# Exercise Palindrome: ---Check if word is palindrome (write back the same like usual)---
word = input("Enter a word for check:")
isPal = False
i = 0
while i < len(word)/2:
    print(word[i], word[len(word)-i-1])
    if word[i] != word[len(word)-i-1]:
        isPal = False
        break
    else:
        i += 1
        isPal = True
if isPal:
    print(f"The word {word} is Palindrome.")
else:
    print(f"The word {word} is NOT Palindrome.")