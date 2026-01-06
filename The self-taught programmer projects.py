import random

#Q1-Print three different srtings
print("Hello world! \n")
print("This is the first challenge. \n")
print("Here we go! \n")


#Q2-write a program that prints a message if a var is less than 10, and different message if the var
#is greater than or equal to 10.
var = 11

if var < 10:
    print("The number is less than 10!")

elif var >= 10:
    print("The number is greater or equal to 10!")

#Q3-Write a program that prints a message if a var is less than or equal to 10, another message 
#if the var is greater than 10 but less than or equal to 25, and another message if the var is
#greater than 25.
if var <= 10:
    print("hey!") 

if var > 10 and var <= 25:
    print("Nice!")

if var > 25:
    print("Great!")

#Q4-Create a program that divides two variables and print the remainder

num_1 = int(input("Enter a num: "))
num_2 = int(input("Enter another num: "))

res = num_1 % num_2

print(res)

#Q5-Create a program that takes two variables, divides them, and prints the quotient

numerator=89
denominator=34

quotient= numerator/denominator

print(quotient)

#Q6-Write a program with a var **AGE** assigned to an int that prints different strings depending
#on what integer **AGE** is
 
# range(1, 101) includes numbers 1 through 100
AGE = range(1, 101) 

try:
    pick = int(input("Pick a number from 1 through 100: "))

    if pick not in AGE:
        print("Invalid! Please pick a number between 1 and 100.")
    elif pick <= 25:
        print("This number falls into the first quartile!")
    elif pick >= 75:
        print("This number falls into the third quartile!")
    else:
        print("Hip hip hooray!, the number falls into the interquartile range.")

except ValueError:
    print("Error: Invalid input. Please enter a whole number.")

