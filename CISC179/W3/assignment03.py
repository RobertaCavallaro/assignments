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


