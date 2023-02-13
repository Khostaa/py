# os : module for operating system related features
import os 
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    #print the name of OS
    print(os.name)
    # #prints out nt : which is official name of windows internally

    # #check for item existence and type
    print("Item exists:",str(path.exists("textfile.txt")))
    print("Item is a file:",path.isfile("textfile.txt"))
    print("Item is a directory:",path.isdir("textfile.txt"))

    # #work with file paths
    print("Item's path: ",path.realpath("textfile.txt"))
    print("Item's path and name:",path.split(path.realpath("textfile.txt"))) #splits file name from path

    # Get the modification time
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t) #prints time the file was modified in full date form
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))  #prints numeric time

    #calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been", td,"since the file was modified.")
    print("Or,",td.total_seconds(),"seconds")
if __name__ == "__main__":
    main()