# conversion calulator 
#By: Wyatt Lynch

# user input regarding the length to convert

# get the unit from the user

#convert the length to the correct unit

# output the answer to the user

user_number = float(input("What number to convert? "))
userUnit = input("What unit is your number? ")

# to convert in to mm -- inches x 25.4
# to convert mm to in -- mm / 25.4

#user gives in unit
convNumber = user_number * 25.4

print(convNumber)
print(userUnit)