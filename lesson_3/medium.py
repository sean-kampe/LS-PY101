message = '-The Flintstones Rock!'
for _ in range(10):
    print(message)
    message = '-' + message
# LS solution
for padding in range(1, 11):
    print(f'{"-" * padding}The Flintstones Rock!')

def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    if result == []:
        print('Please enter a positive integer and try again')
    else:
        return result

import math

nan = float('nan')
print(math.isnan(nan))

# paper!
# False!
# True!
