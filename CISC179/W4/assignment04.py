##1a) Take five inputs from an user and save it in a tuple called my_tuple
dato1 = input("what's your name: ")
dato2 = input("how old are you: ")
dato3 = input("how are you: ")
dato4 = input("where are you from: ")
dato5 = input("do you like python: ")

my_tuple = (dato1, dato2, dato3, dato4, dato5)

print("Account is: ")
print(my_tuple)

##tuples are unchangeable!!

######Count the repeated integers and print the result on the console.
my_tuple = (1,2,3,4,3,2,1,2,3,5,4,3,2,1)
print("How many 1:", my_tuple.count(1))
print("How many 2:", my_tuple.count(2))
print("How many 3:", my_tuple.count(3))
print("How many 4:", my_tuple.count(4))
print("How many 5:", my_tuple.count(5))

###1D.Proof that my_tuple in part c is different than the my_tuple in part d.

my_tuple = (1, 2, 3, 4, 3, 2, 1, 2, 3, 5, 4, 3, 2, 1)

print("tuple c ID is: ", id(my_tuple))

my_tuple = my_tuple + my_tuple

print("tuple d ID is: ", id(my_tuple))

##1e. Explain why the following operations aren’t legal for the tuple. Answer without using the Python.
x = (1,2,3,4) 
x.append(1) #you can't add in tuple
x[1] = "hello" # you can't replace in tuple
del x[2] # you can't delete in tuple

#2. Packing and unpacking tuples
#2a. What is the data type of each variable? variables  from the right takes values of the left
#(one, two, three, four) =  (1, 2, 3, 4)
one=1
two=2
three=3
four=4

