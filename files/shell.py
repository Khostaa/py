#for working with filesystem shell methods

import os
from os import path
import shutil  #shell util
from shutil import make_archive
from zipfile import ZipFile
def main():
    #make duplicate of existing path
    if path.exists("textfile.txt.bak"):
        #get the path to the file in current directory
        src = path.realpath("textfile.txt")

        #let's make a backup copy by appendig "bak" to the name
        # dst = src  + ".bak"
        # shutil.copy(src,dst)

        #rename the original file
        # os.rename("textfile.txt","newfile.txt")

        #now put things into ZIP Archive
        # root_dir, tail = path.split(src)
        # shutil.make_archive("archive","zip", root_dir)

        #more fine-grained control over ZIP Files
        with ZipFile("testzip.zip","w") as newzip:
            newzip.write("newfile.txt")
            newzip.write("textfile.txt.bak")

if __name__ == "__main__":
    main()
