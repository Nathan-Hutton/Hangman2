'''
Hangman.py
'''

import sys
import random

class Hangman:
    '''
    Initializes the words list
    '''
    def __init__(self):
        file = open('words.txt','r')
        self.words = []
        self.wordguess = []
        for line in file:
            self.words.append(line.rstrip())

    '''
    Outputs the current status of the guesses
    '''
    def printword(self):
        for c in self.wordguess:
            print(c,end="")
        print()

    def playgame(self):
        # generate random word
        guessed_letters = []
        word = self.words[random.randint(0,len(self.words)-1)]
        #print word
        self.wordguess = ['_'] * len(word)

        guesses = 0

        correct = lambda guess: True if guess in word else False

        isRightLen = lambda guess: True if len(guess) == 1 else "Must type a single character"
        inAlpha = lambda guess: True if guess.isalpha() else "Must type a character in the alphabet"
        notGuessed = lambda guess: True if guess not in guessed_letters else "Character already guessed"

        while guesses < 10:
            print("Guesses: " + str(guesses))
            self.printword()
            ch = input('Enter a guess: ').lower()
            print(ch)

            valid = map(lambda func: func(ch), [isRightLen, inAlpha, notGuessed])
            invalid = False
            for i in valid:
                if i != True:
                    print(i)
                    invalid = True
            if invalid:
                continue

            if correct(ch):
                for i in range(len(word)):
                    if word[i] == ch:
                        self.wordguess[i] = ch
            else:
                print("Guess is incorrect")


            guesses += 1
            guessed_letters.append(ch)
            if '_' not in self.wordguess:
                print("You win")
                break

        if '_' in self.wordguess:
            print("You lost, word is: " + word)

if __name__ == "__main__":

    game = Hangman()

    game.playgame()
