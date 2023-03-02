from colorama import Fore
from turtle import clear

#Asks the user for their name.
person = input(Fore.LIGHTCYAN_EX + "What's your name? ")

#The functions that displays hello + name of the user.
def helloGreeting():
    greeting = print("Hello, {}.".format(person))
    return greeting

#The functions that displays welcome.
def welcome():
    print ("Welcome to calculator..")

#The functions that says Goodbye.
def goodBye():
    print('Goodbye {}. \nHope to modify it real soon:)'.format(person))


#The function that performs the arithmetic operations.
def operation():
    #Asks the user to enter the type of operation he/she wants to perform.
    print("Which operation would you like to operate on? :")
    print("1. Addition(+)")
    print("2. Subtraction(-)")
    print("3. Division(/)")
    print("4. Multiplication(*)")
    print("5. Modulo(%)")

    #Asks the user to select a number from the type of operation.
    operations = int(input("Kindly select an option: ")) 

    #loops that check if the user selected from 1 - 5 of the operations.
    if operations > 0 and operations <= 5:
        #Execute this loops if true
        if(operations == 1):
            print('you have successfully selected {}'.format(operations))
            print('Addition operation')
            a = int(input("your first integer value: "))
            b = int(input("your second integer value: "))
            print('{} + {} = {}.'.format(a, b, (a + b)))
            goodBye()

        elif(operations == 2):
            print('you have successfully selected option {}'.format(operations))
            print("Subtraction operation")
            a = int(input("your first integer value: "))
            b = int(input("your second integer value: "))
            print('{} - {} = {}.'.format(a, b, (a - b)))
            goodBye()

        elif(operations == 3):
            print('you have successfully selected {}'.format(operations))
            print("Division operation")
            a = int(input("your first integer value: "))
            b = int(input("your second integer value: "))
            print('{} / {} = {}.'.format(a, b, (a / b)))
            goodBye()
        
        elif(operations == 4):
            print('you have successfully selected {}'.format(operations))
            print("Multiplication operation")
            a = int(input("your first integer value: "))
            b = int(input("your second integer value: "))
            print('{} * {} = {}.'.format(a, b, (a * b)))
            goodBye()
        
        elif(operations == 5):
            print('you have successfully selected {}'.format(operations))
            print("Modulo operation")
            a = int(input("your first integer value: "))
            b = int(input("your second integer value: "))
            print('{} % {} = {}.'.format(a, b, (a % b)))
            goodBye()

        else:
            proceed = input("Would you like to proceed? \nYes or No: ")
            if (proceed == "Yes" or proceed == "Y" or proceed == "yes" or proceed == "y"):
                print("Nice one {}".format(person))
                operation()

            elif (proceed == "No" or proceed == "N" or proceed == "no" or proceed == "n"):
                print("Thanks for coming {}.".format(person))

            else:
                print("Sorry, try again later.")

    #Execute this line of code if otherwise.
    else:
        print("Seems you have typed a wrong digit of operations.")
        again()

#The function that asks user if he/ she wants to proceed.
def again():
    again = input("Do you wish to continue?\nYes or No: ")
   
    if (again == "Yes" or again == "Y" or again == "yes" or again == "y"):
        print("Nice one! {}".format(person))
        operation()

    elif (again == "No" or again == "N" or again == "no" or again == "n"):
        goodBye()

    else:
        print (Fore.LIGHTRED_EX + "Terminated successfully:/")


helloGreeting()

welcome()

operation()