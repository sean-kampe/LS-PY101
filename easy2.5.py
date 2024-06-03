# Write a program that prompts the user for two positive numbers (floating-point), then prints the results of the following operations on those two numbers: addition, subtraction, product, quotient, floor quotient, remainder, and power. Do not worry about validating the input.

num_1 = float(input("Enter your first float number: "))
num_2 = float(input("Enter your second float number: "))

sum = num_1 + num_2
sub = num_1 - num_2
mult = num_1 * num_2
div = num_1 / num_2
floor = num_1 // num_2
rem = num_1 % num_2
pow = num_1 ** num_2

print(f'==> {num_1} + {num_2} = {sum}')
print(f'==> {num_1} - {num_2} = {sub}')
print(f'==> {num_1} * {num_2} = {mult}')
print(f'==> {num_1} / {num_2} = {div}')
print(f'==> {num_1} // {num_2} = {floor}')
print(f'==> {num_1} % {num_2} = {rem}')
print(f'==> {num_1} ** {num_2} = {pow}')
