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
