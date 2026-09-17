##1a) Take five inputs from an user and save it in a tuple called my_tuple
dato1 = input("what's your name: ")
dato2 = input("how old are you: ")
dato3 = input("how are you: ")
dato4 = input("where are you from: ")
dato5 = input("do you like python: ")

my_tuple = (yellow, pink, red, green, blue)

print("Color is: ")
print(my_tuple)

##tuples are unchangeable!!

######Count the repeated integers and print the result on the console.
my_tuple = (1,2,3,4,3,2,1,2,3,5,4,3,2,1)
print(my_tuple.count(1))
print(my_tuple.count(2))
print(my_tuple.count(3))
print(my_tuple.count(4))
print(my_tuple.count(5))

###1D.Proof that my_tuple in part c is different than the my_tuple in part d.
#they have different ids

my_tuple = (1, 2, 3, 4, 3, 2, 1, 2, 3, 5, 4, 3, 2, 1)

print(id(my_tuple))

my_tuple = my_tuple + my_tuple

print(id(my_tuple))

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

#2b. Python has an extended unpacking feature, allowing an element marked with * to absorb any number of elements not matching the other elements. For example,
x = (1, 2, 3, 4)
a, b, *c = x
a, b, c
(1, 2, [3, 4])

#2c. What will be the result of a, *b, c = x?
(1,[2,3],4)

#3. Memory management
my_x = [100,200,300,400]
my_y = (200,300,400,500)
#Discuss how memory addresses are assigned to each index of the list and the tuple. Pay attention to new addresses & re-used addresses.
#Instead of duplicating data, Python copies only the address to locate it and to save memory

