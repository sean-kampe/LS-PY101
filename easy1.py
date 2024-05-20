
#Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

def integer(number):
    if abs(number) % 2 == 0:
        return False
    return True

