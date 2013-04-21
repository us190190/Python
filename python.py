#!/usr/bin/python

############# WHILE LOOP ###############

print '============================'

print 'Guess a number'

while True:

    user_number = int(raw_input('Enter a number : '))

    if user_number==10:

        print 'guessed correct'

        break

    elif user_number==11 or user_number==9:

        print 'close enough'

    else:

        print 'sorry'

else:

    print 'while loop over'

   

############# FOR LOOP ###############

print '============================'

start = int(raw_input('Enter starting : '))

end = int(raw_input('Enter ending : '))

for i in range(start, end+1):

    print i

else:

    print 'for loop ends'

############# FUNCTIONS ###############

print '============================'

def get_product(n1, n2):

    return n1*n2

number = int(raw_input('Enter an integer : '))

for i in range(1, 11):

    print number, ' * ', i, ' = ', get_product(number, i)

############# LOCAL v/s GLOBAL VARIABLE ###############

print '============================'

def change_x(x):

    x+=2

    print 'X inside is : ', x

x=50

change_x(x)

print 'X outside is : ', x

print '============================'

def change_x():

    global x

    x+=2

    print 'X inside is : ', x

x=50

change_x()

print 'X outside is : ', x

############# DEFAULT ARGUMENTS FOR FUNCTIONS ###############

print '============================'

def get_table(number, start=1, end=10):

    for i in range(start, end+1):

        print number, ' * ', i, ' = ', number*i

get_table(4)

print '============================'

get_table(5, 1, 5)

print '============================'   

get_table(start=5, number=1, end=8)

print '============================'   

get_table(end=3, number=1)

