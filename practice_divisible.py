__author__ = 'taozi'
def cube(number):
    return number ** 3
def by_three(number):
    if number % 3 == 0 and number != 0 :
        print number ** 3
        return cube(number)
    elif number == 0:
        print "please input a number"
    else:
        print "the number couldn't be divisibled"
        return False

by_three(33)
