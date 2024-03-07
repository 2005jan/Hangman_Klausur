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
for i in word:
    print(i,"",end="")

#############################
#       functions           #
#############################

#############################
#       main                #
#############################

#############################
#       result              #
#############################