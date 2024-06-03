# Write a function that takes a short line of text and prints it within a box.

def print_in_box(text):
    length = len(text) + 2
    spaces = length * ' '
    dashes = length * '-'
    if text == '':
        print('+--+\n|  |\n|  |\n|  |\n+--+')
    else:
        print('+' + dashes + '+')
        print('|' + spaces + '|')
        print('| ' + text + ' |')
        print('|' + spaces + '|')
        print('+' + dashes + '+')

print_in_box('To boldly go where no one has gone before.')

#
#+--------------------------------------------+
#|                                            |
#| To boldly go where no one has gone before. |
#|                                            |
#+--------------------------------------------+
#
print_in_box('')

#
#+--+
#|  |
#|  |
#|  |
#+--+
#
# You may assume the output will always fit in your terminal window.

print_in_box('Hi')