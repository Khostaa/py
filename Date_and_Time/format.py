from datetime import datetime

def main():
    #Times and dates can be formatted using a set of predefined string
    #control codes
    now = datetime.now()

    ##DATE FORMATTING##

    # %y %Y - Year, %a %A - weekday, %b %B - month, %d = day of month
    # Capital B gives name of month
    # Capital Y gives full date of year
    # Capital A give full name of weekday

    # str f time
    print(now.strftime("The Current year is: %Y"))
    print(now.strftime("%a, %d %B, %y"))

    # %c - locale's date and time
    print(now.strftime("Locale date and time: %c"))

    #  %x - locale's date
    print(now.strftime("Locale date: %x"))

    # %X - locale's time
    print(now.strftime("Locale time: %X"))


    ### TIME FORMATTING ###

    # %I/%H - 12/24 Hour
    # %M - minute
    # %S - second
    # %p - locale's AM/PM
    print(now.strftime("Current time: %I:%M:%S %p")) 
    print(now.strftime("Current time: %H:%M")) 

if __name__ == "__main__":
    main()