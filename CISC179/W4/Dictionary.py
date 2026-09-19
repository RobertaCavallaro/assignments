
#1a) Create dictionary of your choice of keys and values. Create dictionary size of 10 elements.

travel_list = {
    "January": "Edinburgh",
    "March": "Manchester",
    "April": "Madrid",
    "June": "Helsinki",
    "August": "Iceland",
    "September": "HongKong",
    "November": "Seoul",
    "December": "Prague",
    "February": "Catania",
    "October": "Vienna"
}

# 1b. Take inputs from a user and add them in a dictionary called my_user_dict.
new_month = input("Insert month: ")
new_city = input("Insert city: ")

# add the first input todictionary
travel_list[new_month] = new_city

#ask if they want to continue
ask = input("Do you want to continue (Y/N)? ")

#if they say yes show the new outputs
if answer == "Y" or answer == "y":
    new_month2 = input("Insert month: ")
    new_city2 = input("insert city: ")
    
    # add second input to dictionary
    travel_list[new_month2] = new_city2
    
    answer = input("Do you want to continue (Y/N)? ")

print(travel_list)
