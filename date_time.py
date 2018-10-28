from datetime import datetime

# Use a function called, datetime.now to retrieve the current date n datetime
print (datetime.now())

# Extracting Information
# What if you don't want the entire date and month?
now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day

print (current_year)
print (current_day)

# What if we want to print like this: mm/dd/yyyy
# % operator after the string will fill the %02d and %04d placeholders in the string on the left with the numbers and strings in the parentheses on the right.
# %02d pads the month and day numbers with zeros to two places, and %04d pads the year to four places. This is one way dates are commonly displayed.
print ('%02d-%02d-%04d' % (now.month, now.day, now.year))

# Hours, Minutes, and Seconds
print (now.hour)
print (now.minute)
print (now.second)

print ('%02d:%02d:%02d' % (now.hour, now.minute, now.second))

# Print date and time on the same line in single print statement
print ('%02d-%02d-%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second))
