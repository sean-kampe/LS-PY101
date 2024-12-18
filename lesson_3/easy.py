# numbers = [1, 2, 3]
# numbers[6] = 5
# this will raise an error, there is no index 6

def ends_with_exclamation(string):
    print(True) if string[-1] == '!' else print(False)

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

ends_with_exclamation(str1)
ends_with_exclamation(str2)


famous_words = "seven years ago..."
new_words = "Four score and " + famous_words
print(new_words)
new_words_2 = f"Four score and {famous_words}"
print(new_words_2)

munsters_description = "the Munsters are CREEPY and Spooky."
print(munsters_description.lower().capitalize())

munsters_description_2 = "The Munsters are creepy and spooky."
munsters_description_3 = ''
for letter in munsters_description_2:
    if letter.isupper():
        munsters_description_3 += letter.lower()
    else:
        munsters_description_3 += letter.upper()
print(munsters_description_3)

str3 = "Few things in life are as important as house training your pet " \
       "dinosaur."
str4 = "Fred and Wilma have a pet dinosaur named Dino."
print('Dino' in str3)
print('Dino' in str4)

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append('Dino')
print(flintstones)

flintstones.extend(['Jim', 'Hoppy'])
print(flintstones)

advice = "Few things in life are as important as house training your pet dinosaur."
print(advice.split('house')[0])
print(advice.replace('important', 'urgent'))

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
new_numbers = numbers[::-1]
new_numbers_2 = list(reversed(numbers))

numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)
print(number1 in numbers)
print(number2 in numbers)

value = 42
for _ in range(10, 101):
    if _ == value:
        print('YES')
        break
    elif _ == 100:
        print('no')

second_value = 101
for _ in range(10, 101):
    if _ == second_value:
        print('YES')
        break
    elif _ == 100:
        print('no')

# Above code works, but this is so much better
print(42 in range(10, 101))

more_numbers = [1, 2, 3, 4, 5]
del more_numbers[2]
print(more_numbers)

table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}
print(isinstance(more_numbers, list))
print(isinstance(table, list))

title = "Flintstone Family Members"
centered_title = title.center(40)

statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."
print(statement1.count('t'))
print(statement2.count('t'))

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
print('Spot' in ages)
additional_ages = {'Marilyn': 22, 'Spot': 237}
ages.update(additional_ages)
print(ages)

nums = [1, 2, 3, 4]
nums.clear()
del nums[:]

print([1, 2, 3] + [4, 5])

string1 = "hello there"
string2 = str1
string2 = "goodbye!"
print(string2)

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)

def is_color_valid(color):
    return color == "blue" or color == "green"
def is_color_valid_2(color):
    colors = ['blue', 'green']
    return color in colors
print(is_color_valid_2('green'))