from sys import argv

script, filename = argv

print "We're going to read {}".format(filename)
print "Press any button to continue..."

raw_input('?')

print "Opening the file..."
target = open(filename, 'r')

print target.read()

print "Closing the file..."
target.close()
