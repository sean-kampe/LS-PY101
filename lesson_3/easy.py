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