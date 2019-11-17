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

     #while user error entry rerurn question
    while error_entry < 8 :

        letter = input("enter a letter :")
        if letter == word:
            test = 8
            print("you find the word")
            break
             #stop the loops if find word


        #for good letter find i replace the * in list by letter
        if letter in list1:
            #i use the index elem and enumerate for verify the letter
            for index, elem in enumerate(list1):
                if elem == letter:
                    # i add the letter in the list as same index of letter
                    hidden_list[index] = elem
                    # i use join method for return the hidden list
                    letter_in_word = ''.join(hidden_list)
                    print(letter_in_word)
        # compare the list
        if list1 == hidden_list:
            print("you find the word")
            test = test
            break # i stop the loops

            return saves_scores
        else:
            print("you have {} try".format(8-error_entry))
            # i adding one to error entry for error enter letter
            error_entry += 1
            test = -1
        if error_entry == 8:
            print("you loose")
            break

            #print(saves_scores)

def colect_score(name, saves_scores,score, test):
    """this function registered the score in files with pickle
    and reead this files """
    score = {name: test}
    with open("score", "wb") as fichier:
        scores = pickle.Pickler(fichier)
        scores.dump(saves_scores)

    with open("score", "rb") as fichier:
        scores = pickle.Unpickler(fichier)
        liste_recuperer = scores.load()
        print(liste_recuperer)
        return liste_recuperer

    print(score)
    print(colect_score(name, scores))
    # i dont find the soluce for this function
