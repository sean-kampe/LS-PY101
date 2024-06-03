
# Write a function that takes a positive integer, n, as an argument and prints a right triangle whose sides each have n stars. The hypotenuse of the triangle (the diagonal side in the images below) should have one end at the lower-left of the triangle, and the other end at the upper-right.

def triangle(num):
    spaces = ' ' * num
    spaces = spaces[1:]
    stars = '*'
    while num > 0:
        print(spaces + stars)
        num -= 1
        spaces = spaces[1:]
        stars += '*'

triangle(5)
#
#    *
#   **
#  ***
# ****
#*****
#
triangle(9)
#
#        *
#       **
#      ***
#     ****
#    *****
#   ******
#  *******
# ********
#*********