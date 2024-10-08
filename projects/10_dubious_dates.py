#Exercise 1: Write a Python program that prints the current date and time using the datetime module.
from datetime import date
 #imports dates
my_date = date.today()

print(my_date) #print function

#Exercise 2: Write a Python program that prints the current date and time using the datetime module. Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)

import datetime

# Get the real time date 
now = datetime.datetime.now()

# Format the date in MM/DD/YYYY format
formatted_date = now.strftime("%m/%d/%Y")

# Print 
print("Current Date:", formatted_date)
print("Current Time:", now.strftime("%H:%M:%S"))

#Exercise 3:Using the strptime function, convert two strings into dates. Then find the difference in days between the two.
from datetime import datetime

# Define the date strings
date_string1 = "2023-10-01"
date_string2 = "2023-10-07"

# Convert strings to datetime objects
date_format = "%Y-%m-%d"
date1 = datetime.strptime(date_string1, date_format)
date2 = datetime.strptime(date_string2, date_format)

# Calculate the difference in days
difference = (date2 - date1).days

# Print the difference
print(f"The difference in days between {date_string1} and {date_string2} is {difference} days.")
