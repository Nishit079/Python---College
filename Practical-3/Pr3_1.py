#Write a program to check if number is Armstrong.
num = input("Enter the number to check whether it is armstrong or not:\n")

l = len(num)
num = int(num)

temp = num
sum = 0

while temp != 0:
    sum = sum + (temp % 10) ** l
    temp = temp // 10

if sum == num:
    print(f"Number {num} is an Armstrong number")
else:
    print(f"Number {num} is not an Armstrong number")

