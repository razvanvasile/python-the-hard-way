# From the module sys import the variable argv
from sys import argv

# unpack the script name and file name
filename = 'ex15_sample.txt' # 'raw_input("> ")

# open the file with "filename", returns a file object
txt = open(filename)

# print a simple message, and read the contents of the file
print "Here's your file %r:" % filename
print txt.read()

# record the name of the second file to open
print "Type the filename again:"
file_again = raw_input("> ")

# open the file
txt_again = open(file_again)

# print its contents
print txt_again.read()
