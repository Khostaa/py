# 'w' : for writing
# 'r' : for reading
# 'a' : for appending

def main():
    #open a file for writing and create it if it doesn't exist
    myfile = open("textfile.txt","w+")
    #open takes two arguments
    # - 1st argument is filename
    # - 2nd argument is operation to perform
    # in the case above, it open file "textfile.txt" for writing operation and creates if it doesn't exist already.

    # Open the file for appending the text to end
    myfile = open("textfile.txt", "a+") #opens file for appending
    # write some lines of data to the file
    for i in range(10):
        myfile.write("This is some new text\n")

    #close the file when done
    myfile.close()

    #open file back up and read the content
    myfile = open("textfile.txt","r")
    if myfile.mode == 'r':
        contents = myfile.read()  # to read all content of file at once
        print(contents)
        fl = myfile.readlines() # for reading file line by line
        for x in fl: #prints all the contents of file line by line
            print(x)
if __name__ == "__main__":
    main()