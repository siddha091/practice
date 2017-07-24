'''
Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.",
        "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas",
        "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization,
        and spacing are usually ignored.
'''

import re


def is_palindrome(inputString):
    # Removing all the special characters.
    inputString = re.sub('[^a-zA-Z0-9]', '', inputString)

    # Reversing the string.
    reversedString = inputString[::-1]

    # print(inputString.lower())
    # print(reversedString.lower())

    # Comparing the strings.
    if inputString.lower() == reversedString.lower():
        return True
    else:
        return False


print ("Enter the string to check palindrome:")

stringToCheckPalindrome = input()
if is_palindrome(stringToCheckPalindrome) == True:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")