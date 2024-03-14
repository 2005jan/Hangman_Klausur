#############################
#       author: Jan         #
#       date: 07.03.2024    #
#############################

#Game Hangman

#############################
#       imports             #
#############################

import random

#############################
#       variables           #
#############################

from word import word  #variable word is assigned with words from word.py
word=random.choice(word)    # chooses random word out of list
print(word)
guessed_letters=[]   
lives=6             #temp

#############################
#       functions           #
#############################
def print_word():
    for letters in word:    #prints "_" for every letter in word
        print("",end="_")

def user_guess(guess):
    if guess in guessed_letters:    #checks if this letter was already guessed before
        print("Double input")
    else:
        guessed_letters.append(guess)
        if guess not in word:
            global lives
            lives = lives-1
            print("",end="")
    for letter in word:
            if guess==letter:    
                print("TRUE")
    print(f"Letters guessed till now:{guessed_letters}")
    if all(letter in guessed_letters for letter in set(word)):
        print("won")
        return 
            
def user_input():
    while lives>0 and not all(letter in guessed_letters for letter in set(word)):
        input_guess=input("\nGeben Sie einen Buchstaben ein: ")   #user inputs a letter
        input_guess=input_guess.upper()     #capitalizes user input
        user_guess(input_guess)

#############################
#       main                #
#############################

print()
user_input()
if lives==0:
    print("lost")
#############################
#       result              #
#############################