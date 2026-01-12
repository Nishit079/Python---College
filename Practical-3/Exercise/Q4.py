#Develop a program that takes a word and displays it in the following pattern (example for word 'PYTHON'):
#P
#PY
#PYT
#PYTH
#PYTHO
#PYTHON
#PYTHO
#PYTH
#PYT
#PY
#P



word = input("Enter word: ")

for i in range(1, len(word) + 1):
    print(word[:i])

for i in range(len(word) - 1, 0, -1):
    print(word[:i])

