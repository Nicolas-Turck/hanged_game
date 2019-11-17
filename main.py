from random import *
from donnees import *
from fonctions import *
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
        #call function to masqued word choice
        hidden_list = masqued_word(list1, word, hidden_list)
        print(''.join(hidden_list))
        #call function game with many parameters
        play_game(name, word,hidden_list, list1)
        #call function colect score for save the score of user
        #colect_score(name, score)
        #print(liste_recuperer)

    #if player_choice == "2":
        #colect_score(name, saves_scores)
        #print(liste_recuperer)


    if player_choice == "3":
        print("good bye {}".format(name))
        exit()
