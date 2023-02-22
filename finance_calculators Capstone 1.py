# This is a programme written in Python

# User chooses one of two calculators: investment calculator ('investment') or a home loan repayment calculator ('bond')

import math #import module for calculations

# Print instructions for the user to the terminal
print('''\nType either 'investment' or 'bond' to choose from the menu:\n 
investment - to calculate the amount of interest you'll earn on your investment 
bond - to calculate the amount of interest you'll have to pay on a home loan\n''')

# Ask the user to choose calculator
choice = input("Please enter your choice: ")

# Account for different input formats
choice = choice.lower()

if choice == "investment":

    deposit = float(input("How much money are you depositing? "))
    rate = float(input("Enter the interest rate as a percentage: "))
    years = float(input("How many years do you plan to invest for? "))
    interest = input("Simple or compound interest? ")
    interest = interest.lower()
    if interest == "simple":
        total = round(deposit*((1+(rate/100))*years)) #calculates total using formula
    elif interest == "compound":
        total = round(deposit*math.pow(1+(rate/100), years))
    else:
        print("Input error. Try again.")
    print("Your total investment is R" + str(total))

elif choice == "bond":

    value = float(input("What is the present value of the house? "))
    rate = float(input("Enter the annual interest rate as a percentage: "))
    monthly_rate = (rate/12)/100 #as a percentage
    months = float(input("How many months do you plan to take to repay the loan? "))
    repayment = round((value*monthly_rate) / (1 - (1+monthly_rate)**(-months))) #calculates monthly repayment
    print("The monthly repayment will be R" + str(repayment))

else:
    print("Error. Please choose 'bond' or 'investment'") #Return error if 'bond' or 'investment' isn't entered