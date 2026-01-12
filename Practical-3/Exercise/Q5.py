st = input("Enter string: ")
words = st.split()
sum = 0

for i in range(len(words)):
    num_str = ""

    for ch in words[i]:
        if ch.isdigit():
            num_str += ch

    if num_str != "":
        num = int(num_str)
        sum += num
        words[i] = words[i].replace(num_str, str(num * num))

print("Sum of numbers:", sum)
print("Modified string:", " ".join(words))


