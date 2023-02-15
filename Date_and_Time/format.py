from datetime import datetime

def main():
    #Times and dates can be formatted using a set of predefined string
    #control codes
    now = datetime.now()

    ##DATE FORMATTING##

    # %y %Y - Year, %a %A - weekday, %b %B - month, %d = day of month
    print(now.strftime("The Current year is: %Y"))



if __name__ == "__main__":
    main()