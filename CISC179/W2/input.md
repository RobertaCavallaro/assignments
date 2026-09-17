#kilograms to pounds kg = float(input("Enter your weight in kilograms: ")) #convert kg to pounds pounds = kg * 2.2 #result print("Your weight in pounds is :", pounds)

#variables for credit card assignment netBalance = float(input("Enter the net balance: ")) payment = float(input("Enter the payment: ")) d1 = int(input("Enter number of days in the first billing cycle (d1): ")) d2 = int(input("Enter number of days payment in second billing cycle (d2): ")) interest_rate = float(input("Enter the interest rate (e.g., 0.0152): "))

#calculate daily average averageDailyBalance = (netBalance * d1 - payment * d2) / d1 #calculate iterest interest = averageDailyBalance * interest_rate #result print("The final interest rate is:", interest)

####c. Distance Between Two Cars

ask user for average speed
speed1= float(input(" Enter the average speed for car A")) speed2= float(input(" Enter the average speed for car B")) #ask for hours hours = int(input("Enter the hours passed: ")) #ask for minutes minutes=int(input("Enter the minutes passed: ")) #convert time to hours total_hours= hours + (minutes/60.0) #calculate distance distance1= speed1total_hours distance2= speed2total_hours #calculate shortest distance using pythagorean theorem short_distance= math.sqrt((distance12)+ (distance22)) #result print("The shorterst distance between the two cars is: ", short_distance)

#Troubleshooting

a. hello = "hello"# valid variable name assigned to string b. _var = 100# valid variable name staring with underscore,assigned to literal c. !var_1 = 200 # not valid variable cant start with special characters d. print = "print me" # not valid cause it is missing the brackets () e. False = 0 #reserve word that cannot be used as a variable

https://docs.python.org/3/library/functions.html#input
