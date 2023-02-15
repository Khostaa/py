from datetime import date
from datetime import time
from datetime import datetime

def main():
    #date objects
    #get todays's dater from simeple today() method from date class
    today = date.today()
    print("Today's date is ",today)

    #print out the date's individual components
    print("Date componenets: ", today.day, today.month, today.year)

    #retrieve today's weekday(0: Monday, 6: Sunday)
    print("Today's weekday # is",today.weekday())
    days = ["mon","tue","wed","thur","fri","sat","sun"]
    print("Which is a ", days[today.weekday()])

    #DATETIME OBJECTS

    # Get Today's date from datetime class
    today = datetime.now()
    print("The Current date and time is ",today)

    #Get the current time
    t = datetime.time(datetime.now())
    print("The Current Time is ",t)

if __name__ == "__main__":
    main()