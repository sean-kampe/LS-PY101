# Write a function that takes one argument, a positive integer, and returns a string of alternating '1's and '0's, always starting with a '1'. The length of the string should match the given integer.

def stringy(num):
    checker = '1'
    new_string = ''
    for element in range(num):
        new_string += checker
        if checker == '1':
            checker = '0'
        else:
            checker = '1'
    return new_string
print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True