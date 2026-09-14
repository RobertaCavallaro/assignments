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
#########################################
#c. Implement the grading scheme for the CISC 179 course. The grading scheme as follows:

# Ask user to insert percentage as integer
percentage = int(input("Enter your percentage: "))

# Check the percentage to find grade and description
if percentage > 90:
    grade = "A"
    description = "Work of genuinely superior quality."

elif percentage >= 80:
    grade = "B"
    description = "Passing performance falls approximately in the upper distribution of passing grades."

elif percentage >= 71:
    grade = "C"
    description = "Passing performance falls approximately in the center of the distribution of all passing grades."

elif percentage >= 65:
    grade = "D"
    description = "Passing performance falls approximately in the lower distribution of passing grades."

else:
    grade = "F"
    description = "Failing performance that does not satisfy the basic requirements of the course and needs to be improved in significant ways."

# Show final grade
print("Grade is:", grade)
print("Description is:", description)

#d. Write a code which takes and, or, not as an user input. Create a truth table by writing your expressions. Display the truth table using print() function. Research how the truth tables for logical operators are structured.

# Ask user for the logical operator
operator = input("Enter a logical operator: ")

if operator == "and":
    print("A      | B      | Result")
    print("------------------------")
    print("True   | True   |", True and True)
    print("True   | False  |", True and False)
    print("False  | True   |", False and True)
    print("False  | False  |", False and False)

elif operator == "or":
    print("A      | B      | Result")
    print("------------------------")
    print("True   | True   |", True or True)
    print("True   | False  |", True or False)
    print("False  | True   |", False or True)
    print("False  | False  |", False or False)

elif operator == "not":
    print("A      | Result")
    print("---------------")
    print("True   |", not True)
    print("False  |", not False)

else:
    print("Wrong. You must enter 'and', 'or', or 'not'")

#e. To determine whether an integer is even or odd using only a bitwise AND operator. the user will input an integer. Your code should utilize the bitwise AND operator to differentiate between even and odd numbers. Finally, use the print() function to display the result. Avoid using any modulus or remainder operators.
# Ask user to input integer
number = int(input("Enter integer: "))

# Check if the number is even or odd using bitwise AND (&)
if (number & 1) == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#6.Code revision
# Ask user for their name and the time
name = input("What is your name? ")
time = int(input("What time is it? "))

# Check if user entered a valid time (between 0 and 24:00)
if time >= 0 and time <= 2400:
    
    #Check if the time is before 12:00
    if time < 1200:
        print("Hi " + name + ", good morning!")
        
    #Check if it's before 6:00 pm
    elif time < 1800:
        print("Hi " + name + ", good afternoon!")
        
    #If it is not morning of afternoon, then must be evening
    else:
        print("Hi " + name + ", good evening!")
        
#If time is less than 0 or greater than 24:00, then it's invalid
else:
    print("Invalid time. Please enter a time between 0 and 2400.")

# This prints at the very end, no matter what path the code took above
print("Good Bye")

#7. one two


#1. While loop
#a. Please write Python code using a while loop to perform the following steps.
n0 = int(input("enter a number: "))
steps = 0

while n0 != 1:
    if n0 % 2 == 0:
        n0 = n0 // 2
    else:
        n0 = 3 * n0 + 1      
    print(n0)
    steps += 1
print("steps =", steps)

#b. Write code that uses a while loop and runs indefinitely. Modify the same code to resolve the infinite loop issue.
count = 30

# Set condition to True for infinite
while count <= 35:
    print("The infinite number is:", count)
    count += 30

print("Finished!")

#c. Write a program that takes two integers as input and asks the user to choose an arithmetic operation to perform with those numbers. At the end of the program, prompt the user with the question, "Do you want to continue?" If the user selects "Y" or "y," the program should restart; otherwise, it should exit and display the message, "Have a good day."
count = "y"

while count == "y" or count == "Y":
    number1 = int(input("Enter one number: "))
    number2 = int(input("Enter second number: "))
    
    operators = input("Pick one arthmetic operator between +, -,*, /: ")
    
    if operators == "+":
        print("Output:", number1 + number2)
    elif op == "-":
        print("Output:", number1 - number2)
    elif op == "*":
        print("Output:", number1 * number2)
    elif op == "/":
        print("Output:", number1 / number2)
        
    count = input("Would you like to continue (Y/N): ")

print("Have a good day!")

#2.FOR LOOPS
###########
# Ask for an input and make it lowercases
write = input("Enter your input: ")
write = write.lower()

count_letter = 0

# Count letters 
for char in write:
    # Check if it is a letter from a to z
    if char >= 'a' and char <= 'z':
        count_letter += 1

print("Total number of alphabets:", count_letter)
print("Total number of distinct alphabets are: ")

######a. Using a range function, generate a list of 100 integers and assign the list to my_list. Verify that the variable my_list data type is list. Use your favorite four methods and apply on the list. You can find the methods on Python Docs.
# generate a list of 100 integers and assign the list to my_list.
my_list = list(range(1, 100))

# Verify that the variable my_list data type is list
print("The data type is:", type(my_list))

# Use your favorite four methods and apply on the list.
# append method
my_list.append(102)
print("After .append(101), the last item is:", my_list[3])

#insert method
my_list.insert(0, 200)
print("After .insert(0, 201), the first item is:", my_list[0])

#pop method
popped_number = my_list.pop()
print("The .pop() method removed this number from the end:", popped_number)

#reverse method
my_list.reverse()
print("First 5 items after using .reverse():", my_list[0:2])

###########################
#b. Suppose that you have a list of 10 items long. How might you move the last three items from the end of the list to the beginning, keeping them in the same order?
#10 items list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# We slice the list into two parts and add them together in reverse order
new_list =list[-4:] + list[:-4]

print("My list is :", list)
print("New list is :", new_list)

#### len([[1,2]] * 3) = 3

####d. Create a list my-list-ten of 10 items that includes some duplicate entries. Then, generate a second list my-list-ten-mem that contains the memory addresses of the items from the list my-list-ten. Use Python to research and identify the unique and duplicate memory addresses.

# Create a list of 10 items with some duplicates
my_list_ten = [10, 25, 35, 25, 48, 25, 59, 60, 60, 71]

# Generate a second list containing the memory addresses
# id() function gets the memory address of each item on the list
my_list_ten_mem = []

for item in my_list_ten:
    mem_address = id(item)
    my_list_ten_mem.append(mem_address)

print("List of items:    ", my_list_ten)
print("List of mem addresses:   ", my_list_ten_mem)
print("-" * 50)

#Identify unique and duplicate memory addresses
unique = []
duplicate = []

for address in my_list_ten_mem:
    # Count how many times a mem address show in the list
    mem_show = my_list_ten_mem.count(address)
    
    # If it only appears once, it is unique
    if mem_show == 1:
        unique.append(address)
        
    # If it shows more than once means is a duplicate
    elif mem_show > 1 and address not in duplicate:
        duplicate.append(address)

print("Unique memory addresses:")
for addr in unique:
    print(addr)

print("Duplicate memory addresses:")
for addr in duplicate:
    print(addr)
#e. Delete the list my-list-ten created in the above step.
del my_list_ten

#g.What code could you use to get a copy y of that list in which you could change the elements without the side effect of changing the contents of x?
import copy
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Create a copy
y = copy.deepcopy(x)
y[0][0] = 99
print("x:", x) 
print("y:", y) 

####  H. yes it is possible, for loops and if conditions
#### I. there are 9 spaces
######## LIST OPERATIONS
#append
items = ["laptop", "book"]
items.append("pen")

print(items) 

#extend 
items = ["laptop", "book"]
more_items = ["pencil", "watch"]
items.extend(more_items)
print(items) 

#remove
items = ["laptop", "book","pen"]
items.remove("pen")
print(items) 


#sort alphabetically
items = ["laptop", "book","pen","headphones","calculator"]
items.sort()
print(items) 

#clear
items = ["laptop", "book","pen","headphones","calculator"]
items.clear()
print(items) 




