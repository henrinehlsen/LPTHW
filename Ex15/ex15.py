#from sys import argv

# defines two strings for argv's input
#script, filename = argv

# opens a file and puts its content into "txt"
#txt = open(filename)


#prints a message about what the file is named
#print "Here is your file %r:" % filename
# prints the content of that file
#print txt.read()

# a prompt
print "Type the filename again:"
# creates a variable, storing the rawinput in it, after putting an arrow
file_again = raw_input(">> ")
# puts the content of the file into a new variable
txt_again = open(file_again)


# prints the contents of the new variable
print txt_again.read()
