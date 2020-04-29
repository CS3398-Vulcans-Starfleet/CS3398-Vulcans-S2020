#Python file to delete an entire folder/directory
import os
import send2trash

#take a file path from the user
user_input = raw_input("Enter the path of your file: ")
os.chdir(user_input)

#checking to see if the file exists
if os.path.exists(user_input):
    #safley sends the entire directory to the trash bin
    send2trash.send2trash(user_input)
else:
    print "the file does not exist"

