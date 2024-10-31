#Ask for someone's age, if they are less than 0 (they accidentally gave you a negative, ask again)

#You can also break loops by using booleans and the break statement.

#while True:
#    age = int(input("Give me your age. "))
#    if age < 0:
#        print("You have given me age that is less than 0. Please try again.")
#    else:
#        break
#print("Your age is", age,".")

#while True:
#    try:
#        age = int(input("Give me your age "))
#        if age < 0:
#            raise ValueError
#        break
#    except ValueError:
#        print("Input invalid. Please enter a positive integer.")