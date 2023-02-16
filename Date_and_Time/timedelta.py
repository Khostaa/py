## Given a particular date, you may want to calculate relative to that date in the future or the past, for that we can use TimeDelta Class in Python
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365,hours=5,minutes=1))

# print today's date
now = datetime.now()
print("Today is", now)

# print today's date one year from now
print("one year from now it will be", str(now + timedelta(days=365)))

#create a timedelta that uses more than one argument
print("In two weeks and 3 days it will be", str(now + timedelta(weeks = 2, days = 3)))

# Calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d %Y")
print("One week ago it was", s)

### How many days until April Fools' Day?
today = date.today()
afd = date(today.year,4,1)

# use date comparision to see if April Fool's has already gone this year
# if it has use the replace() function to get the date for next year
if afd <today:
    print("April Fools' Day already went by:", ((today-afd)).days)
    afd = afd.replace(year = today.year + 1)
# now calculate the amount of time until April Fool's Day
time_to_afd = afd - today
print("It is",time_to_afd," days until the next April Fools' Day!")

