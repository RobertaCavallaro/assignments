#W2-3/4 Programming variables

1. VARIABLE MEMORY USAGE
var1 = 10

check for memory address for var1
print("Var1 address (value 10):", hex(id(var1)))

var1 = 100

Check for memory address for var1 value 100
print("var1 address (value 100):", hex(id(var1)))

var2 = 100

Check the memory address for var2
print("var2 address (value 100):", hex(id(var2)))

2. MEMORY MAP
str1 = "Hello" str2 = "World"

Find out the memory addresses of each character in str1
print("Addresses for 'Hello':") print("H:", hex(id(str1[0]))) print("e:", hex(id(str1[1]))) print("l:", hex(id(str1[2]))) print("l:", hex(id(str1[3]))) print("o:", hex(id(str1[4])))

Find out the memory addresses of each character in str2
print("\nAddresses for 'World':") print("W:", hex(id(str2[0]))) print("o:", hex(id(str2[1]))) print("r:", hex(id(str2[2]))) print("l:", hex(id(str2[3]))) print("d:", hex(id(str2[4])))

3. PROBLEM-SOLVING
x = "dog" y = "cat"

print("x + y:", x + y) print("Sentence:", "the " + x + " chases the " + y) print("x * 4:", x * 4)

Incrementing a value by 1
x = 50 x = x + 1 # increments x by 1 print("Number used for increment:", x)

#Troubleshooting a. hello = "hello" # ok because variable name is valid and it is assigned to a string

b. _var = 100 # ok variable name with underscore is valid and it is assigned to a literal

c. !var_1 = 200 # not valid because the variables cannot start with special characters

d. print = "print me" # not valid cause it is missing the brackets ()

e. False = 0 #reserve word that cannot be used as a variable
