from random import *
from donnees import *
import pickle
def nameUser():
    """this function resquest the name of
    player and return the name or 
    declare a pseudo if user no entry name""" 
    name = input("enter your name :")
    if name == "":
        name = "cartman"
    return name

def menu():
    player_choice = input("1:play, 2:score, 3:exit\n enter number choice :")
    return player_choice

def word_choice(liste_mot):
    """this function choice a word in 
    list word in donnees.py for the game and return it"""
    word = choice(liste_mot)
    return word

def masqued_word(list1, word, hidden_list):
    """this function change word to hidden word and return it"""
    # for all element in word
    for elem in word:
        # i adding elem in list1
        list1.append(elem)
        #i adding * in hidden list for elem
        hidden_list.append("*")
        #i display the hidden list with join method
    return hidden_list 

def play_game(name, word, hidden_list, list1):
    """ this function is the game with verify letter and calculate score"""
    error_entry = 0
    test = 8
    score = {name: test}
     #while user error entry rerurn question
    while test !=1:
        letter = input("enter a letter :")
        
        if letter not in list1:
            error_entry = +1
            #update test
            test= test- error_entry
            #update score
            score = {name: test}
            print(score)
            print("no letter in word you have {} try".format(test-error_entry))    
        #if letter in list1:
        if letter in list1:    #i use the index elem and enumerate for verify the letter 
            for index, elem in enumerate(list1):
                if elem == letter:
                    # i add the letter in the list as same index of letter 
                    hidden_list[index] = elem
                    # i use join method for return the hidden list
                    letter_in_word = ''.join(hidden_list)
                    print(letter_in_word)
                    print("you have {} try".format(test-error_entry))
        
        if list1 == hidden_list:
            test= test-error_entry
            score = {name: test}
            print('you find the word ')
            print(score)
            colect_score(name, score, test)
            liste_score_txt(name, score, test)
            break
                
        if test == 1:
            score = {name: 0}
            print("you loose ")
            print(score)
            #call function with register score with pickle
            colect_score(name, score, test)
            #call function to register score in txt files
            liste_score_txt(name, score, test)
            break
    return score      
    
def liste_score_txt(name, score, test):
    """this function register score in txt files"""
    score = score
    scores = str(score)
    #open or create files in txt for register score
    with open("score.txt", "a") as files:
        files.write(scores)
     
        
def colect_score(name, score, test):
    """this function registered the score in files with pickle 
    and reead this files """
    score = score
    scores = pickle.dumps(score)
    with open("scores_players", "wb") as files:
       files.write(scores)
        
     
    
def read_scores():
    """open and reead the score with Unpickle"""
    with open("scores_players", "rb") as files:
        scores_players = files.read()
        liste_score = pickle.loads(scores_players)
        print(liste_score)
    """ open and read the files score txt"""
    with open("score.txt", "r") as files:
        liste_score = files.readlines()
        print(liste_score)