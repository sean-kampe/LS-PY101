
# Build a program that randomly generates and prints Teddy's age. To get the age, you should generate a random number between 20 and 100, inclusive.

import random

def age():
    age = random.randint(20, 100)
    return (f'Teddy is {age} years old!')

print(age())