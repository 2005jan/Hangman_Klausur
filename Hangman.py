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
    if guess not in word:
            global lives
            lives = lives-1
            print("",end="")
    for letter in word:
            if guess==letter:    
                print("TRUE")
    print(f"Sie haben bisher die Buchstaben {guessed_letters} versucht.")
    if all(letter in guessed_letters for letter in set(word)):
        print("won")
        return 
            
def user_input():
    while lives>0 and not all(letter in guessed_letters for letter in set(word)):
        while True:
            input_guess=input("\nGeben Sie einen Buchstaben ein: ")   #user inputs a letter
            input_guess=input_guess.upper()     #capitalizes user input
            alphabet=input_guess.isalpha()      #alphabet is only True when the input is in the alphabet
            if input_guess in guessed_letters:    #checks if this letter was already guessed before
                print("Diesen Buchstaben haben Sie bereits versucht.")
            elif len(input_guess) == 1 and alphabet==True:    #checks if the input is only one letter
                guessed_letters.append(input_guess)     #adds guess to guessed_letters
                user_guess(input_guess)
            else:
                 print("Falsche Eingabe! Bitte geben Sie nur einen Buchstaben ein.")

#############################
#       main                #
#############################

print_word()
user_input()
if lives==0:
    print("lost")
#############################
#       result              #
#############################