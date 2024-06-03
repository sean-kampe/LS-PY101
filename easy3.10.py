
# Write a function that takes a year as input and returns the century. The return value should be a string that begins with the century number, and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.
#
# New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th century.

def century(year):
    century = str(year)
    if year <= 100:
        return '1st'
    if year <= 200:
        return '2nd'
    if year <= 300:
        return '3rd'
    if str(year)[-1] == '0':
        century = str(int(str(year)[:-2]))
    if str(year)[-1] != '0':
        century = str(int(str(year)[:-2]) + 1)
    if century[-1] == '1' and century[-2] != '1':
        return century + 'st'
    if century[-1] == '2' and century[-2] != '1':
        return century + 'nd'
    if century[-1] == '3' and century[-2] != '1':
        return century + 'rd'
    else:
        return century + 'th'


print(century(2000) == "20th")          # True
print(century(2041) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True
print(century(112) == "2nd")        # True
print(century(2001) == "21st")          # True
print(century(2241) == "23rd")          # True