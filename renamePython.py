#Renames all the files in a folder/directory for better sorting
import os

#take a file path from the user
user_input = raw_input("Enter the path of your directory: ")

#checking to see if the file exists
if os.path.exists(user_input):
    os.chdir(user_input)
else:
    print "the directory does not exist"

#listdir creates a list of all the files
for f in os.listdir(user_input):
    #splitting up the different parts of the file name
    f_name, f_ext = os.path.splitext(f)
    #parsing at the -
    f_title, f_brand, f_num = f_name.split('-')
    #striping away empty spaces
    f_title = f_title.strip()
    f_brand = f_brand.strip()
    #stripping empty space, stripping the pound sign by starting at the second character, padding the numbers with a 0
    f_num = f_num.strip()[1:].zfill(2)
    #setting up the new format from the listed filenames and setting it to a variable
    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
    #renaming the files still inside the for loop
    os.rename(f, new_name)
