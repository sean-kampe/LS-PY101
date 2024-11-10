def prompt(message):
    print(f'==> {message}')

def invalid_integer(number_str):
    try:
        int(number_str)
        if int(number_str) == 0:
            return True
    except ValueError:
        return True
    except TypeError:
        return True
    return False

def invalid_rate(rate):
    try:
        float(rate)
    except ValueError:
        return True
    except TypeError:
        return True
    return False

def bad_rate(rate):
    if float(rate) > 1 or float(rate) < 0:
        return True
    return False

prompt('Hello this is a mortgage calculator that determines monthly '
       'interest! Lucky you!')
more = True

while more:
    prompt('Enter the loan amount rounded to the dollar: ')
    loan_amount = input()

    while invalid_integer(loan_amount):
        prompt('Please enter a valid loan amount rounded to the nearest '
              'dollar: ')
        loan_amount = input()
    prompt('Enter the monthly interest rate in decimal format: ')
    interest_rate = input()

    while invalid_rate(interest_rate) or bad_rate(interest_rate):
        prompt('Please enter the monthly interest rate in decimal format '
               'between 0.0 and 1.0: ')
        interest_rate = input()

    monthly = float(interest_rate) / 12
    prompt('Enter the loan duration in years: ')
    full_duration = input()

    while invalid_integer(full_duration):
        prompt('Please enter loan duration in whole number years: ')
        full_duration = input()

    duration = int(full_duration) * 12
    if monthly == 0:
        monthly_payment = round(int(loan_amount) / duration, 2)
    else:
        monthly_payment = int(loan_amount) * (monthly / (1 - (1 + monthly) ** (-duration)))
    monthly_payment = round(monthly_payment, 2)

    prompt(f'Your monthly payment is : ${monthly_payment}')
    prompt('Would you like to do another loan operation? Enter 1 for yes: ')
    more = input()

    if more != '1':
        more = False
        print('Thanks for using the mortgage calculator!')