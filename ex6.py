# define x
x = "There are %d types of people." % 10
# define binary
binary = "binary"
# define do_not
do_not = "don't"
# define y
y = "Those who know %s and those who %s." % (binary, do_not)

# print the content of x on the screen
print x
# print the content of y on the screen
print y

# print I said x on the screen with using r format
print "I said: %r." % x
# print I said y on the screen wotj isomg string format
print "I also said: '%s'." % y

# define hilarious bool
hilarious = False
# define joke_evaluation with adding a format too
joke_evaluation = "Isn't that joke so funny?! %r"

# print joke_evaluation with adding hilarious to replace the format
print joke_evaluation % hilarious

# define w
w = "This is the left side of..."
# define e
e = "a string with a right side."

# print em out
print w + e
