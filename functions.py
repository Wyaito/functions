# conversion calulator 
#By: Wyatt Lynch

# user input regarding the length to convert
user_number = float(input("What number to convert? "))
# get the unit from the user
userUnit = input("What unit is your number? ")
#convert the length to the correct unit
if(userUnit == "in"):
    #perform in to mm
    convNumber = user_number * 25.4
    convUnit = 'mm'
elif(userUnit == 'mm'):
    #perform mm to in
    convNumber = user_number / 25.4
    convUnit = 'in'
else: 
    print('that is not a valid unit')
# output the answer to the user
print(convNumber, convUnit)





