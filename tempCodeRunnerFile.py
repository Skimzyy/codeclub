import random

matricNumber = input("What's your Matric number? ")
number = len(matricNumber)
string = 'abcdefghujklmnopqrstuvwxyz0123456789'

def generatePassword():
    if (int(matricNumber) == number):
        get = " "
        for i in range(8):
            get += string[random.randint(0, 36)]
        print("Your password is: {} ".format(get))
    else:
        print("Terminated")

generatePassword()