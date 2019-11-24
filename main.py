from random import *
from donnees import *
from fonctions import *
import pickle

print("welcome to hanged game")

# call function for user entry name
list_score_all = []
name = nameUser()
score = {}
test = 0
print("lets go {}".format(name))
while 1:
    
    player_choice = menu()
    if player_choice == "1":
        #score = {}
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
    #function display score in txt files   
    if player_choice == "2":
        read_scores()
        
    if player_choice == "3":
        print("good bye {}".format(name))
        exit()
