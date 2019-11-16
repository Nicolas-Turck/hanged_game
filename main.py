from random import *
from donner import *
from functions1 import *
import pickle

print("welcome to hanged game")

# call function for user entry name
name = nameUser()
score = {}
test = 8
print("lets go {}".format(name))

while 1:
    player_choice = menu()

    if player_choice == "1":
        list1 = []
        # i create a hidden list for adding the word hidden
        hidden_list= []
        #call function for choice word
        word = word_choice(liste_mot)
