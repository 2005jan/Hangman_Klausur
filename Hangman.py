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

#chooses a random word from word.py and returns it as word into main
def init():
    from word import word               #variable word is assigned with words from word.py
    random_word=random.choice(word)     # chooses random word out of list
    return random_word

#prints the already guessed letters of the random word
#prints unguessed letters as underscores
#prints remaining lifes 
def print_word():
    for i in word:                              #is run once for each letter in the random word
        if i in guessed_letters:                #checks whether the letter entered is contained in the word 
            print(i, end=" ")                   #prints the letter in the right spot(s)
        else:
            print("_", end=" ")                 #print underscore for every unguessed letter
    print(f"\nSie haben noch {lifes} Leben")    #remaining lifes are printed

#collects user input
#checks if input is valid. Passes valid inputs to user_guess()
#checks if user wants to stop the program
def user_input():
    global lifes,next_round
    #runs until no lives are left or the word has been guessed
    while lifes>0 and not all(letter in guessed_letters for letter in (word)):
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
            lifes=0
        else:                                                           #no valid input
            print("Falsche Eingabe! Bitte geben Sie einen Buchstaben ein.")  

#checks if guessed letter is in word
#returns user which letters have already been used
#returns user information about score
#checks if game has been won or lost            
def user_guess(guess):
    global lifes,score,next_round
    #checks if guessed letter is in word
    if guess in word:
        count=word.count(guess)     #counts amount of correctly guessed letters
        score+=count                #adds the value of count to score
    else: 
        lifes -=1                   #reduces lifes 
        score-=1                    #reduces score
    print_word()
    print(f"Sie haben bisher die Buchstaben {guessed_letters} versucht.")
    print(f"Punktzahl: {score}")
    #checks if game has been won or lost 
    if all(letter in guessed_letters for letter in set(word)):
        score+=5
        print(f"\nGlückwunsch! Sie haben das Wort {word} erraten.\nSie haben {score} Punkte.\n")
        return 
    elif lifes==0:
        print(f"Sie haben keine Leben mehr! Das Wort war {word}.")
        next_round=False

#############################
#       main                #
#############################
            
while next_round==True:     #program ends if a round was lost or the quit was entered
    lifes=6                 #lifes is declared in the first run and reset in the next runs
    guessed_letters=[]      #guessed_letters is declared in the first run and reset in the next runs
    word=init()
    print_word()
    user_input()
