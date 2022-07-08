inp=input("Do you want to play: ")
if inp=='y':
    while(True):
        a=input("Enter the number: ")
        if a=='q':
            break
        try:
            a=int(a)
            b=1/a
            print(b)


        except ValueError as g:
            print("Exception 1 occured!")
            print("Use a valid number!!")

        except ZeroDivisionError as g:
            print("Exception 2 occured!")
            print("Please enter a value other than zero")

else: 
    print("Thanks for playing")