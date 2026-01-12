#Write a python program to count odd numbers from given three numbers and display maximum odd number.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

odd_count = 0
max_odd = None

# Check first number
if a % 2 != 0:
    odd_count += 1
    max_odd = a

# Check second number
if b % 2 != 0:
    odd_count += 1
    if max_odd is None or b > max_odd:
        max_odd = b

# Check third number
if c % 2 != 0:
    odd_count += 1
    if max_odd is None or c > max_odd:
        max_odd = c

print("Count of odd numbers:", odd_count)

if odd_count > 0:
    print("Maximum odd number:", max_odd)
else:
    print("No odd numbers entered.")
