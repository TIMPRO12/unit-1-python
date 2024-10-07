from datetime import datetime
from datetime import date
from datetime import time
#all of these allows me to use the date and time features

"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
my_dati = datetime.now() #this show's the current time
print(my_dati)

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
my_dt = datetime.now()
my_st = my_dt.strftime('%m/%d/%Y') #this will print the date in a specific way
print(my_st)

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""





"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""


"strftime.org" #very good website