#############################
#                           #
#          HANGMAN          #
#                           #
#############################
#       author: Jan         #
#  student number:1351461   #
#       date: 07.03.2024    #
#  brief: Hangman in German #
#       endless runner      #
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

#prints instructions
def start():
    print("\nSie spielen Galgenmännchen. \nDas Ziel ist es, eine höchstmgliche Anzahl an Punkten zu erreichen.")
    print("Gesucht werden deutsche Nomen. Bitte beachten Sie, dass Umlaute ersetzt worden sind: ä -> ae, ö -> oe, ü -> ue, und ß -> ss.")
    print("Um das Spiel später zu verlassen, geben Sie bitte 'quit' ein.")
    temp=input("Bitte geben Sie eine beliebige Eingabe ein, um fortzufahren.")

#chooses a random word from word.py and returns it as word into main
def init():
    from word import word               #variable word is assigned with words from word.py
    random_word=random.choice(word)     # chooses random word out of list 'word' 
    return random_word

#prints the already guessed letters of the random word
#prints unguessed letters as underscores
#prints remaining lives 
def print_word():
    for i in word:                              #is run once for each letter in the random word
        if i in guessed_letters:                #checks whether the letter entered is contained in the word 
            print(i, end=" ")                   #prints the letter in the right spot(s)
        else:
            print("_", end=" ")                 #print underscore for every unguessed letter
    print(f"\nSie haben noch {lives} Leben")    #remaining lives are printed

#collects user input
#checks if input is valid. Passes valid inputs to user_guess()
#checks if user wants to stop the program
def user_input():
    global lives,next_round
    #runs until no lives are left or the word has been guessed
    while lives>0 and not all(letter in guessed_letters for letter in (word)):
        input_guess=input("\nGeben Sie einen Buchstaben ein: ")   
        input_guess=input_guess.upper()                                 #capitalizes user input
        alphabet=input_guess.isalpha()                                  #alphabet is only True when the input is in the alphabet
        if input_guess in guessed_letters:                              #checks if this letter was already guessed before
            print("Diesen Buchstaben haben Sie bereits versucht.")
        elif len(input_guess) == 1 and alphabet==True:                  #checks if the input is only one letter
            guessed_letters.append(input_guess)                         #adds guess to guessed_letters
            user_guess(input_guess)
        elif input_guess=="QUIT":                                       #stops 'while' loop in main and stops program if input is 'quit'
            next_round=False
            lives=0
        else:                                                           #no valid input
            print("Falsche Eingabe! Bitte geben Sie einen Buchstaben ein.")  

#checks if guessed letter is in word
#returns user which letters have already been used
#returns user information about score
#checks if game has been won or lost            
def user_guess(guess):
    global lives,score,next_round
    #checks if guessed letter is in word
    if guess in word:
        count=word.count(guess)     #counts amount of correctly guessed letters
        score+=count                #adds the value of count to score
    else: 
        lives -=1                   #reduces lives 
        score-=1                    #reduces score
    print_word()
    print(f"Sie haben bisher die Buchstaben {guessed_letters} versucht.")
    print(f"Punktzahl: {score}")
    #checks if game has been won or lost 
    if all(letter in guessed_letters for letter in set(word)):
        score+=5                    #bonus for guessing the word
        print(f"\nGlückwunsch! Sie haben das Wort {word} erraten.\nSie haben {score} Punkte.")
        print("Um das Spiel zu verlassen, geben Sie bitte 'quit' ein.\n")
        return 
    elif lives==0:
        print(f"Sie haben keine Leben mehr! Das Wort war {word}.")
        next_round=False            #stops 'while' loop in main

#############################
#       main                #
#############################
start()                                 
while next_round==True:     #program ends if a round was lost or the quit was entered
    lives=6                 #lives is declared in the first run and reset in the next runs
    guessed_letters=[]      #guessed_letters is declared in the first run and reset in the next runs
    word=init()
    print_word()
    user_input()
