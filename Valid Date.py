# Write a program that reads a date from input and validates that it is a valid date


from datetime import datetime
test_str = '04-01-2025'
print("The original string is : " + str(test_str)) 
format = "%d-%m-%Y" 
res = True
try:
    res = bool(datetime.strptime(test_str, format))
except ValueError:
    res = False
print("Does date match format? : " + str(res))