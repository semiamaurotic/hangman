# Hangman script
import csv
import random
import console
import subprocess as sp


def getword():
    # difficulty = input('Enter difficulty: Easy or Hard') # future: add word length filter.
    with open('wordlist.csv') as csvfile:
        wordreader = csv.reader(csvfile)
        words = [row[0].strip() for row in wordreader]

    words_dict = {}
    for word in words:
        if len(word) in words_dict:
            # append the new number to the existing array at this slot
            words_dict[len(word)].append(word)
        else:
            # create a new array in this slot
            words_dict[len(word)] = [word]

    del words_dict[2]
    del words_dict[3]
    k = random.choice(list(words_dict.keys()))
    word = random.choice(words_dict[k])
    return word


def checkguess(guess, word):
    if guess in word:
        return True
    else:
        return False


def getguess(display, guessed):
    guess = input('{}\n\nPick a letter\n>>> '.format(' '.join(display)))
    while not guess.isalpha() or len(guess) != 1:
        guess = input('enter a single letter\n>>> ')
    while guess in guessed:
        guess = input('Already guessed, pick another letter\n>>> ')
    guessed.append(guess)
    return guess


def showguess(guessed, word):
    display = []
    for letter in word:
        if letter in guessed:
            display.append(letter)
        else:
            display.append('_')
    return display


def main():
    art = {}
    art[7] = '    _______        \n' \
             '   |/      |       \n' \
             '   |               \n' \
             '   |               \n' \
             '   |               \n' \
             '   |               \n' \
             '   |               \n' \
             '___|___            \n'
    art[6] = '    _______        \n' \
             '   |/      |       \n' \
             '   |      (_)      \n' \
             '   |               \n' \
             '   |               \n' \
             '   |               \n' \
             '   |               \n' \
             '___|___            \n'
    art[5] = '    _______        \n' \
             '   |/      |       \n' \
             '   |      (_)      \n' \
             '   |       |       \n' \
             '   |               \n' \
             '   |               \n' \
             '   |               \n' \
             '___|___            \n'
    art[4] = '    _______        \n' \
             '   |/      |       \n' \
             '   |      (_)      \n' \
             '   |       |       \n' \
             '   |       |       \n' \
             '   |               \n' \
             '   |               \n' \
             '___|___            \n'
    art[3] = '    _______        \n' \
             '   |/      |       \n' \
             '   |      (_)      \n' \
             '   |      \|       \n' \
             '   |       |       \n' \
             '   |               \n' \
             '   |               \n' \
             '___|___            \n'
    art[2] = '    _______        \n' \
             '   |/      |       \n' \
             '   |      (_)      \n' \
             '   |      \|/      \n' \
             '   |       |       \n' \
             '   |               \n' \
             '   |               \n' \
             '___|___            \n'
    art[1] = '    _______        \n' \
             '   |/      |       \n' \
             '   |      (_)      \n' \
             '   |      \|/      \n' \
             '   |       |       \n' \
             '   |      /        \n' \
             '   |               \n' \
             '___|___            \n'
    art[0] = '    _______        \n' \
             '   |/      |       \n' \
             '   |      (_)      \n' \
             '   |      \|/      \n' \
             '   |       |       \n' \
             '   |      / \      \n' \
             '   |               \n' \
             '___|___            \n'

    movesleft = 7
    word = getword()
    guessed = []
    display = showguess(guessed, word)

    while movesleft > 0 and '_' in display:
        console.clear()
        print('Guessed: {}\n'.format(' '.join(guessed)))
        print(art[movesleft])
        guess = getguess(display, guessed)
        display = showguess(guessed, word)
        print(' '.join(display))
        if not checkguess(guess, word):
            movesleft -= 1

    console.clear()
    if movesleft > 0:
        print('YOU WON!')
    else:
        print('GAME OVER\nThe word was: {}'.format(word))
        print(art[movesleft])
    again = input('Play again? y/n ')
    if again == 'y':
        main()
    else:
        console.clear()


if __name__ == '__main__':
    main()