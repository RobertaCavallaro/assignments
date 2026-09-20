
#1a. The user selects kilometers per liter (kpl), and the response will be provided in miles per gallon (mpg). The units must be interchangeable, so the program will ask the user whether to convert from kpl to mpg or vice versa.


def conversion (direction, *values):

    conversion2 = 2.352145833

    for value in values:

        try:
            number = float(value)

            if number <= 0:
                print("Error: Please enter a number greater than 0.")
                continue

            if direction == "1":
                result = number * conversion2
                print(number, "kpl =", round(result, 2), "mpg")

            elif direction == "2":
                result = number / conversion2
                print(number, "mpg =", round(result, 2), "kpl")

            else:
                print("You can select only 1 or 2.")

        except ValueError:
            print("Only numbers are allowed")



choice = input("Choose a conversion (1 or 2): ")

values_input = input("Enter values separated by commas: ")

values = values_input.split(",")

conversion (choice, *values)

##############
#1b. How would you write a function that could take any number of unnamed arguments and print their values out in reverse order?
def items_list(*args):
    for items in reversed(args):
        print(items)


items_list("Italy", "Finland", "Iceland", "Sweden")

#1c. What would be the result of changing a list or dictionary that was passed into a function as a parameter value? Which operations would be likely to create changes that would be visible outside the function? What steps might you take to minimize that risk?
########
def new_list(my_list):
    my_list.append("California")


states = ["Colorado", "Utah", "Texas"]

new_list(states)

print(states)

###1d. Assuming that x = 5, what will be the value of x after funct_1() below executes? After funct_2() executes? x = 2


###2. troubleshooting!
def my_func(a,b,**c): ##**c is for keyword arguments, needs a name assigned to a value
  print(c)

my_func(1,2,3,4,5,6) ##3,4,5,6 are positional arguments 

#we use *c to get positional values.

###Using the following code, x should print 100 but it prints 10, why?
### because x=100 is inside the function, in order to print 100 you must write it outside the function


x = 10

def my_func_global():
    global x
    x = 100


my_func_global()

print(x)




