#Python file to delete files
import os

#take a file path from the user
user_input = raw_input("Enter the path of your file: ")

#checking to see if the file exists
if os.path.exists(user_input):
    os.remove(user_input)
    print "File deleted"
else:
    print "the file does not exist"


