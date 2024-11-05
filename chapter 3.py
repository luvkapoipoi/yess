#python if else elif exercies

Score = int(input("Enter you score: "))

if Score > 59: 
    print ("you passed")
else:
    print ("you failed awhh")

age = int(input("Enter your age: "))

if age >= 18:
    print ("You adult")
    
else:
    print ("you not adult")

marks = int(input("Enter your marks: "))

if marks >= 90:
    print ("Grade A")
elif marks >= 75:
    print ("Grade B")
elif marks >= 60:
    print ("Grade C")
else:
    print ("Grade F")

# and operater ==

num = int(input("Enter a number: "))

if num > 0 and num < 10:
    print (" The number is a single digit positive number")
else:
    print (" The number is either negative or has more than one digit")

# checking even or odd

num = int(input("Enter your number: "))

if num % 2 == 0:
    print (f"{num} is an even number ")
else:
    print (f"{num} is an odd number ")

# nested "if-else"

number = int(input("Enter your number: "))

if number >= 0:
    if number == 0:
        print ("The number is zero")
    else:
        print ("The number is positive")
else:
    print ("The number is negative")

# This code checks if your number is either zero, negative or positive using nested if-else statements

#Real Life Scenarios
# Restaurant order discount

bill = int(input("Enter your bill: "))

if bill % 10 <= 50:
    print (f"{bill} is your new bill")

else:
    print ("Your bill no hab discount")