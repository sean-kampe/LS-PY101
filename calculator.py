def prompt(message):
    print(f'==> {message}')
def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False
def invalid_operation(number_str):
    if number_str not in ['1', '2', '3', '4']:
        return True
    return False
prompt('Hello! This is a calculator!')
more = True
while more:
    prompt('Enter your first number: ')
    num_1 = input()
    while invalid_number(num_1):
        print('Hmmm, try entering a number!')
        num_1 = input()
    prompt('Enter your second number: ')
    num_2 = input()
    while invalid_number(num_2):
        print('Hmmm, try entering a number!')
        num_2 = input()
    prompt("Enter the number for your operation to perform: 1) addition;  2) subtraction; 3) multiplication; 4) division: ")
    operation = input()
    while invalid_operation(operation):
        print('Hmmm, try entering a operation using numbers 1-4')
        operation = input()
    match operation:
        case '1':
            result = float(num_1) + float(num_2)
        case '2':
            result = float(num_1) - float(num_2)
        case '3':
            result = float(num_1) * float(num_2)
        case '4':
            result = float(num_1) / float(num_2)
    prompt(f'Your answer is {result}')
    prompt('Would you like to do another operation? Enter 1 for yes: ')
    more = input()
    if more != '1':
        more = False
        print('Thanks for using calculator!')
