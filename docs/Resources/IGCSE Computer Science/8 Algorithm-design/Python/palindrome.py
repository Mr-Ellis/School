word = input("Enter word: ")
wordLength = len(word)
isPalindrome = True

for i in range(0, wordLength):
    if word[i] != word[wordLength-i-1]:
        isPalindrome = False

print("Palindrome? ", isPalindrome)
