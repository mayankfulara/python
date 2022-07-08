# SO WHAT IS HAPPENING IN THIS PROGRAM IS THAT WE ARE TAKING A NUMBER AS INPUT AND IF THE NUMBER IS GREATER THAN 6 AND IF THE USER GIVES AN INPUT OTHER THAN INTEGER THAN OUR CODE WILL DIE AND THROW AN ERROR SO IN ORDER TO TACKLE THOSE ERRORS WE USE THE CONCEPTS OF ERROR HANDLING TO DEAL WITH THESE Z 
while(True):
    print("Press q to quit")
    a=input("Enter a number: ")
    if a=='q':
        break
    try:
        print("Trying!")
        a=int(a)
        if a>6:
            print("The number you entered is greater than 6!!")
    except Exception as e:
        print(f"Your input resulted in an error: {e}")

print("Thanks for playing the game :)")