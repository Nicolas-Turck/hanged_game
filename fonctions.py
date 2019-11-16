from random import *
from donner import *
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
