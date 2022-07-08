''' SO WHAT WE HAVE DONE HERE IS THAT WE HAVE GIVEN A ALTERNATIVE TO OUR FUNCTION THAT IN ANY CONDITION WE DO NOT PASS A NAME THAN THE VALUE STRANGER WILL BE PASSED'''


def greet(name="stranger"):
    print("Hello  "+name)
name1=input("Enter your name: ")
greet("mayank")
greet(name1)
greet()