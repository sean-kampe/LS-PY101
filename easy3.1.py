
# Write a function that takes two arguments, a string and a positive integer, then prints the string as many times as the integer indicates.

def repeat(string, num):
    while num > 0:
        print(string)
        num -= 1
repeat('Hello', 3)