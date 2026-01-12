#Write a program that takes a string input and creates a new string by replacing:
#all vowels with '*'
#all digits with '#'
#all spaces with '_'
st = input("Enter string: ")
new = ""

for ch in st:
    if ch.lower() in 'aeiou':
        new += '*'
    elif ch.isdigit():
        new += '#'
    elif ch == ' ':
        new += '_'
    else:
        new += ch

print("Original:", st)
print("Modified:", new)

