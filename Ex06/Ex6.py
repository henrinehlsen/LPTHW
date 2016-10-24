

# this creates a variable that prints a statement and adds a string
x = "There are %d types of people" % 10
# a variable with a string
binary = "binary"
# this avoids the problem with the single-quotes
do_not = "don't"
# creates a variable with a string and two other strings in it
y = "Those who know %s and those whi %s." % (binary, do_not)

# print the variables content
print x
print y

# print both strings
print "I said: %r." % x
print "I also said: '%s'." % y


hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# first print the variable, after, insert the other one
print joke_evaluation % hilarious

# define two strings
w = "This is the left side of..."
e = "a string with a right side."

# print those.
print w + e
