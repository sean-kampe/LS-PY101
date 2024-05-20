
#Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip, then print both the tip and the total amount of the bill. You can ignore input validation and assume that the user will enter valid numbers.

def tip():
    bill = float(input("What is the bill?\n"))
    per = float(input("What is the tip percentage?\n"))
    per = per / 100
    tip = per * bill
    total = bill + tip
    print(f'The tip is ${tip}')
    print(f'The total is ${total}')

tip()