x = 200
y = 10
def main():
    if x<y:
        result = x ,' is less than', y
    elif x ==y:
        result = x, 'is equal to',y
    else:
        result = x, 'is greater than',y

    # # "a if C else b"
    result = "x is less than y" if x<y else "x is greater or equal to y"

    print(result)
 #newest comparision tool available from python 3.10
    #match-case makes it easy to compare multiple values 
    value = "three"
    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        case "three" | "four":
            result = (3,4)
        case _:
            result = -1
    print (result)
if __name__ == "__main__":
    main()

