
# Given a string that consists of some words and an assortment of non-alphabetic characters, write a function that returns that string with all of the non-alphabetic characters replaced by spaces. If one or more non-alphabetic characters occur in a row, you should only have one space in the result (i.e., the result string should never have consecutive spaces).

def clean_up(string):
    new_string = ''
    for ele in string:
        if ord(ele) > 96 and ord(ele) < 123:
            new_string += ele
        elif ord(ele) > 64 and ord(ele) < 91:
            new_string += ele
        elif new_string != '' and new_string[-1] == ' ':
            continue
        else:
            new_string += ' '
    return new_string

print(clean_up("---what's my +*& line?") == " what s my line ")
