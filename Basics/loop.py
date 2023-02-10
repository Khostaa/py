def main():
    x = 0
    
    #while loop
    while(x<5):
        print(x)
        x = x+1
    print("New loop from here")
    #for loop
    for x in range(5,10):
        print(x)

    # use for loop over a collection
    days = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
    for d in days:
        print(d)

    # Continue and Break Statements
    for x in range(5,10):
        if x == 7:
            break
        if x%2 == 0:
            continue
        print(x)
    # using enumerate() function to get index
    days = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
    for i,d in enumerate(days):
        print(i,d)

if __name__ == "__main__" :
    main()