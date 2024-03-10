import random

NUM_DIGETS = 3
MAX_GUESS = 10

def getSecretNum():
    # Returns a string of unique random digets that is NUM_DIGETS long.
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGETS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    # Returns a string with the Pico, Fermi, & Bagels clues to the player.
    if guess == secretNum:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'

    clues.sort()
    return ''.join(clues)

def isOnlyDigets(num):
    # Returns True if a num is a string of only digets. Otherwise, return FALSE!
    if num == '':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9 '.split():
            return False

    return True


print('I am thinking of a %s-diget number. Try to guess what it is.' %(NUM_DIGETS))
print('The clues that I give are....')
print('When I say:    That means:')
print('  Bagels       None of the digets are correct.')
print('  Pico         One diget is correct but in the wrong position.')
print('  Fermi        One diget is correct and in the right position.')

while True:
    secretNum = getSecretNum()
    print('I have thought up a number. You have %s guesses to get it.' %(MAX_GUESS))

    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGETS or not isOnlyDigets(guess):
            print('Guess #%s: ' % (guessesTaken))
            guess = input()

        print(getClues(guess, secretNum))
        guessesTaken += 1

        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print('You ran out of guesses. The awnser was %s.' %(secretNum))

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break            