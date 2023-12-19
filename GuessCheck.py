#starting variables
low = 0
high = 100
middle = (low + high)/2
status = False

#ask user to think of a number
print 'Please think of a number between 0 and 100!'
raw_input("Press Enter to continue...")

#validate guess with user
while status == False:
    print 'Is your secret number ' + str(middle) + '?'
    guess = raw_input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. ')

    #if correct
    if guess == 'c':
        status = True
    #if too low
    elif guess == 'l':
        low = middle
        middle = (low + high)/2
    #if too high
    elif guess == 'h':
        high = middle
        middle = (low + high)/2
    else:
        print 'Sorry, I did not understand your input.'

print 'Game over. Your secret number was: ' + str(middle)


