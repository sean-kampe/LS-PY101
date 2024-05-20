
#Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.

num = int(input("Please enter an integer greater than 0: "))
action = input('Enter "s" to compute the sum, or "p" to compute the product: ')
if action == 's':
    total = 0
    for temp in range(num + 1):
        total += temp
    print(f'The sum of the integers between 1 and {num} is {total}.')
if action == 'p':
    total = 1
    for temp in range(1, num + 1):
        total *= temp
    print(f'The product of the integers between 1 and {num} is {total}.')
