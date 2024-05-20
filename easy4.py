
# Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.
#
# Note: 1 square meter == 10.7639 square feet

def area():
    length = float(input('Please enter the length of your room in meters:\n'))
    width = float(input('Please enter the width of your room in meters:\n'))
    meters = length * width
    feet = (meters * 10.7639)
    print(f'The area is {meters} meters or {feet} feet.')

area()
