## Author: Manahari Dahal
## Due Date: October 27
## Class: CSCI 2000
## Instructor: Ms. Greer
## Program Assignment: 8
## Program Title: FunWithFunctions
##
## Program Description: This programs allows user to choose their choice while displaying
##                      different types of design of asterisks 
## Plagiarism Statement:
## I swear that I have not received or given aid on this program
## beyond guidelines of the course including giving or receiving
## specific code conten


def Main(): ## main function and everything is run here
    print("Options: ") ## Layout of the user's output
    print("Pattern 1")
    print("Pattern 2")
    print("Pattern 3")
    print("Pattern 4")
    print() ## prints a new line

    done = False ## done is assigned to False

    while done != True: ## if done is not true then followig condition is applied
        choice = getChoice() ## choice is set to getChoice
        if choice == 1: ## if user enters 1 then
            rows = getRows(choice)          ## rows is set to getRows with choice parameter
            pattern1(rows) ## pattern1(rows) is called
            
        elif choice == 2: ## if user enters 2 then
            rows = getRows(choice)          ## rows is set to getRows with choice parameter
            pattern2(rows) ## pattern2(rows) is called
            
        elif choice == 3: ## if user enters 3 then
            rows = getRows(choice)              ## rows is set to getRows with choice parameter
            pattern3(rows) ## pattern3(rows) is called
            
        elif choice == 4: ## if user enters 4 then
            rows = getRows(choice)              ## rows is set to getRows with choice parameter
            pattern4(rows) ## pattern4(rows) is called
            
        elif choice == 5: ## if user enters 5 then
            done = True                         ## the loop stops
        else: 
            print("You did not enter a valid number.") ## if it is false then it shows an error message that user didn't put a valid number
            print() ## prints a line
            
            
def getChoice(): ## getChoice is defined
    validInput = False ## validInput is set to False

    while not validInput: ## validInput is set
        a = input("Enter 1, 2, 3, or 4 to choose a pattern to display. Enter 5 to exit. ") ## asks user to enter a number they want to enter
        if not a.isdigit(): ## if the user inputs numbers/digits other than 1,2,3,4 or 5 then
            print("Input must be a number")                                             ## it shows an error
            print() ## prints a line
        else: 
            choice = eval(a) ## allows user to input anothr choice
            validInput = True ## validInput is set to true
    return(choice) ## returns the user's desired number


def getRows(choice): ## getRows is defined

    validInput = False ## validInput is set to false

    while not validInput: ## validInput is set
        a = input("\nPattern " + str(choice) + " How many rows (3-20) ") ## asks user to enter a number from 3 to 20
        if not a.isdigit(): ## program doesn't allow user to input any thing other than a number
            print("Input must be a number") ## displays this message
            print() ## prints a line
            print("Values must be between 3 and 20") ## tells user to input number from 3 to 20
            
        else: 
            rows = eval(a) ## allows user to only input a number from 3 to 20
            if rows >= 3 and rows <= 20:
                validInput = True
            else: ## shows this message if user enter any number other than 3 to 20
                print("Values must be between 3 and 20")
    return(rows) ## returns the value of rows

def pattern1(rows): ## pattern 1 is defined to generate a pattern
    for row in range(1,rows+1): ## row's iteration starts from 1
        for col in range(1,rows+1): ## col's iteration starts from 1
            print("*",end="") ## prints asterisks and its design
        print() ## goes to new line
    print() ## prints a line
    

def pattern2(rows): ## pattern 2 is defined to generate a pattern
    for row in range(1,rows+1): ## row's iteration starts from 1
        for col in range(rows-row,0,-1): ## col's iteration starts from number of rows subtracted from the row
            print(" ",end="") ## it creates space
        print("*"*row) ## it prints asterisks with its design
    print() ## prints a line
    
def pattern3(rows): ## pattern 3 is defined to generate a pattern
    for row in range(rows+1,1,-1): ## row's iteration starts from rows to 1 
        for col in range(row,1,-1): ## col runs once
            print("*",end="") ## prints asterisks with its design
        print() ## prints a line
    print() ## prints a line
    
def pattern4(rows): ## pattern 4 is defined to generate a pattern
    for row in range(1,rows+1): ## row's iteration starts from 1
        for col in range(1,2): ## runs once
            print("*" + " " * (row-1) + "*",end="") ## creates space between two asterisks everytime it goes to a new line with additional space
        print() ## prints a line
    print() ## prints a line

Main() ## main function is called and everything is done here
