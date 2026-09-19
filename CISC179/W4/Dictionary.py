
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
if ask == "Y" or ask == "y":
    new_month2 = input("Insert month: ")
    new_city2 = input("insert city: ")
    
    # add second input to dictionary
    travel_list[new_month2] = new_city2
    
    ask = input("Do you want to continue (Y/N)? ")

print(travel_list)
############
#Converting tuples into a dictionary
###########
new_dictionary = [
    ('Name', 'Sarah Connor'),
    ('Date of birth', '1 Jan 1980'),
    ('Address', '1000 Black Mountain Drive', 92126), #too many elements
    ('Name', 'Jim Hawkins')                          #duplicated keys
]

my_dictionary = {}

for elements in new_dictionary:
    if len(elements) != 2:
        print("Too many elements", elements)
        # insert correct values
        keys = input("Input correct key: ")
        elements = input("Input correct element: ")
        
    else:
        keys = elements[0] 
        elements = elements[1]
        
    # check for duplicates
    if keys in my_dictionary:
        print("already exists", elements)
        keys = input("Insert a new element " + str(elements) + ": ")

    my_dictionary[keys] = elements

print(my_dictionary)


# 1e. Count the number of words using a dictionary

text = """The tiger (Panthera tigris) is a large cat and a member of the genus Panthera native to Asia. It has a powerful, muscular body with a large head and paws, a long tail and orange fur with black, mostly vertical stripes. It is traditionally classified into nine recent subspecies, though some recognise only two subspecies, mainland Asian tigers and the island tigers of the Sunda Islands."""


# Convert text into words
words = text.split()

# Create a new dictionary
word_count = {}

#Counting loop
for word in words:
    
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

print(word_count)
