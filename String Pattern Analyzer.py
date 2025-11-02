#Exercise 1.3: String Pattern Analyzer

text = input("Enter a string: ")
totalcahrSpaces = len(text.lower())
totalcharnoSpaces = len(text.lower().replace(" ", ""))
totalcharWithoutSpaces = totalcharnoSpaces
#totalcharWithoutSpaces = totalcahrSpaces
wordCount = len(text.split())
#Most common character (excluding spaces)
textLower = text.lower()
charFrequency = {}
for char in textLower:
    if char in charFrequency:
        charFrequency[char] += 1
    else:
        charFrequency[char] = 1

mostCommonChar = max(charFrequency, key=charFrequency.get)
maxFrequency = charFrequency[mostCommonChar]

#Palindrome check
reversedText = text[::-1].lower()
isPalindrome = text.lower() == reversedText


#Reverse the string

print(f"Total characters (including spaces): {totalcahrSpaces}")
print(f"Total characters (excluding spaces): {totalcharWithoutSpaces}")
print(f"Total words: {wordCount}")
print("Character frequencies:" , charFrequency)
print(f"Most common character : '{mostCommonChar}' appers {maxFrequency} times")
print("#" * 20)
print("Reversed string:", reversedText)
print(f"Is the string a palindrome? {'Yes' if isPalindrome else 'No'}")