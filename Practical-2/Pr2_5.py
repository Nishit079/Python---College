#Write a python program to check if a given character is a vowel or not.

ch = input ("Enter a character that consisting a vowel \n ")

ch = ch.lower()
if ch in ['a' ,'e' ,'i','o','u']:
    print("The entered character is Vowel \n")
else:
    print("The entered character is not consisting a vowel \n")

