a=9   #GLOBAL VARIABLE
def func1():
    global a  #MAKING A LOCAL VARIABLE A GLOBAL VARIABLE
    print(f"Value of a is: {a}")

    a=34     #DECLARING OF A LOCAL VARIABLE
    print(f"Value of a is : {a}")

func1()    #CALLING FUNC1
print(f"Value of a is {a}")