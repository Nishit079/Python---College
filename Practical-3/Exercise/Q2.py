#Create a program that takes a sentence as input and performs the following operations:
#Count total words.Display words containing exactly 5 characters
#Print the position of each vowel in the sentence


st = input("Enter sentence: ")
words = st.split()

print("Total words:", len(words))

print("Words with exactly 5 characters:")
for w in words:
      if len(w) == 5:
       print(w)

print("Vowel positions:")
for i in range(len(st)):
    	      if st[i].lower() in 'aeiou':
                  print(st[i], "at position", i)


