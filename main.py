#Mcdonals BOT
#BOT that takes orders from customers
#programmer : Makee Enricoso



#import library random
import random
import re
#import random interger
from random import randint

#list of names used by BOT
bot_names = ["Joshua", "Martin", "Jake", "Gabi", "Catherine", "Unsavi", "James", "Ethan", "Ron", "Ashera"]



def welcome():
    num = randint(0,9)
    name = (bot_names[num])
    print("***Welcome to Dream Pizza***")
    print("***My name is", name,"***")
    print("***I will be here to help you order youre dlicious Dream Pizza***")

def main():
    welcome()


main() 