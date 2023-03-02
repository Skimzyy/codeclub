#PASSWORD GENERATOR
import random

number = 7
string ='abcdefghijklmnopqrstuvwxyz0123456789'


def generatePassword():
    guesses = 3
    #Condition is True if guess is greater than 3 and the if condition is not met
    while guesses > 0:
        ask = input("What's your Matric number? ")
        #Execute if condition is met or True
        if (len(ask)== number):
            get = " "
            #The loop that returns the length of the password
            for i in range(8):
                #Generates a random password
                get += string[random.randint(0, 36)]
            #Prints the password
            print("Your password is: {} ".format(get))
            break
        #Decreses the number of guesses
        guesses -= 1
    else:
        #Executes if the number of guesses is equal to 3
        print("We couldn't process your request.\nGoodbye!")

#Calling the function
generatePassword()