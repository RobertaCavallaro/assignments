#Your First Python Code
# a. Multiple print() Statements
print("All the world's a stage,")
print("And all the men and women merely players:")
print("They have their exits and their entrances;")
print("And one man in his time plays many parts,")
print("His acts being seven ages.")

# b. Single print() Statement
print("""All the world's a stage,
And all the men and women merely players:
They have their exits and their entrances;
And one man in his time plays many parts,
His acts being seven ages.""")

# Predict the output
print("127", "0", "0", "1", sep=".") #127.0.0.1

#D and E quesstions flush=False buffer the output and flush when the line is terminated with a new line or flush is set to TRUE.
#Literals
print(5 + 2 - 2)
# ___________5______
print(5 / 2)
# _________2.5__________
print(6 // 2) # // integer division
# _________3__________
print(2. * 3)
# __________6.0____________
print(2 < 4)
# __________true_________
print(2 >= 2)
# ___________false________
print("Hello"+"World")
# ________________HelloWorld______
print("bla" * 3)
# _________blablabla______
print(2 * 3 ** 3)
# ______54_____________
print(5 * 25 // 13 + 100 / 2 % 13 // 2)
# _________14.0___________
print(2 * 3 % 5)
# ___________1_________
print((2 % -4), (2 % 4), (2 ** 3 ** 2))
# _______-2 2 512__________


#2. Data type

type("Hello")
# ____string________________
type(1+"2")
# _________Error, you can't add integer and string together______
type(1.)
# ______float______________
type('A')
# _____string_______________
type(500)
# ______integer_____________
type(True)
# _________boolean_________
type("False")
# ______string_____________

#3. Operator precedence
print(10 * 20 % 12 + 30 / -5 * 10 // 8 ** 2)
#7.0

#W2-3/4 Programming variables

# 1. VARIABLE MEMORY USAGE

var1 = 10
# check for memory address for var1
print("Var1 address (value 10):", hex(id(var1)))

var1 = 100
# Check for memory address for var1 value 100
print("var1 address (value 100):", hex(id(var1)))

var2 = 100
# Check the memory address for var2
print("var2 address (value 100):", hex(id(var2)))


# 2. MEMORY MAP
str1 = "Hello"
str2 = "World"

# Find out the memory addresses of each character in str1
print("Addresses for 'Hello':")
print("H:", hex(id(str1[0])))
print("e:", hex(id(str1[1])))
print("l:", hex(id(str1[2])))
print("l:", hex(id(str1[3])))
print("o:", hex(id(str1[4])))

# Find out the memory addresses of each character in str2
print("\nAddresses for 'World':")
print("W:", hex(id(str2[0])))
print("o:", hex(id(str2[1])))
print("r:", hex(id(str2[2])))
print("l:", hex(id(str2[3])))
print("d:", hex(id(str2[4])))


# 3. PROBLEM-SOLVING

x = "dog"
y = "cat"

print("x + y:", x + y)
print("Sentence:", "the " + x + " chases the " + y)
print("x * 4:", x * 4)

# Incrementing a value by 1
x = 50
x = x + 1  # increments x by 1
print("Number used for increment:", x)


#Troubleshooting
a. hello = "hello" # ok because variable name is valid and it is assigned to a string

b. _var = 100 # ok variable name with underscore is valid and it is assigned to a literal

c. !var_1 = 200 # not valid because the variables cannot start with special characters

d. print = "print me" # not valid cause it is missing the brackets ()

e. False = 0 #reserve word that cannot be used as a variable

#kilograms to pounds
kg = float(input("Enter your weight in kilograms: "))
#convert kg to pounds
pounds = kg * 2.2
#result
print("Your weight in pounds is :", pounds)

#variables for credit card assignment
netBalance = float(input("Enter the net balance: "))
payment = float(input("Enter the payment: "))
d1 = int(input("Enter number of days in the first billing cycle (d1): "))
d2 = int(input("Enter number of days payment in second billing cycle (d2): "))
interest_rate = float(input("Enter the interest rate (e.g., 0.0152): "))

#calculate daily average
averageDailyBalance = (netBalance * d1 - payment * d2) / d1
#calculate iterest
interest = averageDailyBalance * interest_rate
#result
print("The final interest is:", interest)

#c. Distance Between Two Cars
# ask user for average speed
speed1= float(input(" enter the average speed for car A"))
speed2= float(input(" enter the average speed for car B"))
#ask for hours
hours = int(input("Enter the hours passed: "))
#ask for minutes
minutes=int(input("Enter the minutes passed: "))

#Troubleshooting

a. hello = "hello"# valid variable name assigned to string
b. _var = 100# valid variable name staring with underscore,assigned to literal
c. !var_1 = 200 # not valid variable cant start with special characters
d. print = "print me"  # not valid cause it is missing the brackets ()
e. False = 0 #reserve word that cannot be used as a variable
