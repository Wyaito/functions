# conversion calulator 
#By: Wyatt Lynch

# user input regarding the length to convert

# get the unit from the user

#convert the length to the correct unit

# output the answer to the user

user_number = float(input("What number to convert? "))
userUnit = input("What unit is your number? ")

if(userUnit == "in"):
    #perform in to mm
    convNumber = user_number * 25.4
elif(userUnit == 'mm'):
    #perform mm to in
    convNumber = user_number / 25.4

print(convNumber)
print(userUnit)