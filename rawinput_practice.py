__author__ = 'taozi'

print 'Welcome to the Pig Latin Translator!'
# Start coding here!
def originalfunc():
    original = raw_input("Enter a word:")
    if len(original) > 0 and original.isalpha() == True:
        print original
    elif len(original) != 0 or original.isalpha() == False:
        print "Only alpha please"
        original = originalfunc()

originalfunc()