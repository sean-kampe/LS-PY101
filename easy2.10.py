
# Build a program that displays when the user will retire and how many years she has to work till retirement.

from datetime import datetime

now = datetime.now()
year = now.year

age = int(input('What is your age?\n'))
retire = int(input('At what age would you like to retire?\n'))

years_left = retire - age
retire_year = year + years_left

print(f"It's {year}. You will retire in {retire_year}. You have only "
      f"{years_left} years "
      f"of "
      f"work "
      f"to go!")
