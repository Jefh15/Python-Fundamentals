# Dates

# We often need current date and time when
# logging errors and saving data

# To get current date and time
# we need to se the datetime library
from datetime import datetime
#save the now datetime in current_date
current_date = datetime.now()
#display the type of current_date
print(type(current_date))

#the now function returns a datetime object
print('Today is: ' + str(current_date))

# There are functions you can use with datetime
# objects to manipulate dates
from datetime import datetime, timedelta
today = datetime.now()
print('Today is: ' + str(today))

# super useful timedelta
#timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

# Use date functions to control date formatting
# day, hour, minutes, seconds, milliseconds
current_date = datetime.now()
print('Day: '+ str(current_date.day))
print('Month: '+ str(current_date.month))
print('Year: '+ str(current_date.year))

print('Hour: '+ str(current_date.hour))
print('Minute: '+ str(current_date.minute))
print('Second: '+ str(current_date.second))

# Sometimes you receive the date as a string
# and need to convert it to datetime object
birthday = input('When is your birthday (dd/mm/yyyy)? ')

# convert string to datetime object
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birthday_date))

# Converting it to a datetime allows
# you to use the date functions
birthday = input('When is your birthday (dd/mm/yyyy)? ')
#strptime(STRING, FORMAT THAT I THINK IT IS)
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birthday_date))
one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day
print('Day before birthday: ' + str(birthday_eve))

# Make sure you add exception
# handlng in case the date entered is invalid
birthday = input('When is your birthday (dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birthday_date))

#one week
one_week = timedelta(weeks=1)
last_week = today - one_week
print('Last week was: ' + str(last_week))