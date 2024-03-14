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

for letters in word:    #prints "_" for every letter in word
    print("",end="_")

def user_input():
    while lives>0:
        guess=input("\nGeben Sie einen Buchstaben ein: ")   #user inputs a letter
        guess=guess.upper()     #capitalizes user input
        if guess in guessed_letters:    #checks if this letter was already guessed before
            print("Double input")
        else:
            guessed_letters.append(guess)
        for letter in word:
            if guess==letter:
                print("TRUE")
            else:    
                lives -=1
                print("",end="")
        print(f"Letters guessed till now:{guessed_letters}")
        if all(letter in guessed_letters for letter in set(word)):
            print("Won")
            return
            


#############################
#       main                #
#############################

user_input()

#############################
#       result              #
#############################