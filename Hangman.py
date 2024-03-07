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
word=random.choice(word)
print(word)

lives=6             #temp
complete=False      #temp

#############################
#       functions           #
#############################

def user_input():
    while lives>0 and complete==False:
        guess=input("Geben Sie einen Buchstaben ein: ")
        for letter in word:
            if guess==letter:
                print("TRUE")
            elif guess=="quit":
                complete==True
            else:    
                print("",end="")


#############################
#       main                #
#############################

user_input()

#############################
#       result              #
#############################