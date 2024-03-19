#############################
#       author: Jan         #
#       date: 07.03.2024    #
# brief: Hangman in German  #
#############################


#############################
#       imports             #
#############################

import random

#############################
#       variables           #
#############################
score=0
next_round=True         

#############################
#       functions           #
#############################
def init():
    from word import word       #variable word is assigned with words from word.py
    random_word=random.choice(word)    # chooses random word out of list
    return random_word

def print_word():
    for i in word:
        if i in guessed_letters:
            print(i, end=" ")
        else:
            print("_", end=" ")
    print(f"\nSie haben noch {lives} Leben")

def user_guess(guess):
    global lives,score,next_round
    if guess not in word:
            lives -=1
            score-=1
    else: 
        count=word.count(guess)
        score+=count
    print_word()
    print(f"Sie haben bisher die Buchstaben {guessed_letters} versucht.")
    print(f"Punktzahl: {score}")
    if all(letter in guessed_letters for letter in set(word)):
        print(f"\nGlückwunsch! Sie haben das Wort {word} erraten.\nSie haben {score} Punkte.\n")
        return 
    elif lives==0:
        print(f"Sie haben keine Leben mehr! Das Wort war {word}.")
        next_round=False

            
def user_input():
    global lives,next_round
    while lives>0 and not all(letter in guessed_letters for letter in (word)):
        input_guess=input("\nGeben Sie einen Buchstaben ein: ")   
        input_guess=input_guess.upper()     #capitalizes user input
        alphabet=input_guess.isalpha()      #alphabet is only True when the input is in the alphabet
        if input_guess in guessed_letters:  #checks if this letter was already guessed before
            print("Diesen Buchstaben haben Sie bereits versucht.")
        elif len(input_guess) == 1 and alphabet==True:    #checks if the input is only one letter
            guessed_letters.append(input_guess)     #adds guess to guessed_letters
            user_guess(input_guess)
        elif input_guess=="QUIT":
            next_round=False
            lives=0
        else:
            print("Falsche Eingabe! Bitte geben Sie einen Buchstaben ein.")  
#############################
#       main                #
#############################
while next_round==True:
    lives=6
    guessed_letters=[]
    word=init()
    print_word()
    user_input()
#############################
#       result              #
#############################