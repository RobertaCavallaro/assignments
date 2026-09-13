#Research and find the ASCII number of all the characters available on the keyboard using Python.
import ascii
print(ascii.charlist())

#a. Find the largest three integers just using if statements. Take user inputs and display the result.
#ask user to input 3 number
numero1 = int(input("Insert first number: "))
numero2 = int(input("Insert second number: "))
numero3 = int(input("Insert third number: "))

#first number is the largest
largest_num= numero1

#if comparison
if numero2 > largest_num:
    largest_num = numero2

if numero3 > largest_num:
    largest_num = numero3
    
#display result
print("largest number is:", largest_num)


#b. Identify multiple methods to determine if a number is even or odd. The user will input an integer, and the output will indicate whether it's "odd" or "even." The code should be organized into sections, with comments separating each part.
# Ask user to insert an integer
random_number = int(input("Enter an integer:"))
#######################
# Modulo Operator using %
#######################
if random_number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#######################
# Bitwise AND Operator (&)
#######################
if (random_number & 1) == 0:
    print(" The number is even")
else:
    print("The number is odd")

#######################
# Integer, Division, and Multiplication
#######################
if (random_number // 2) * 2 == random_number:
    print("The number is even")
else:
    print("The number is odd")


