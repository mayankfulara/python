#GREATEST OF FOUR NUMBERS
#                          ####      METHOD 1        ######
#THE  LOGIC OF THIS PROGRAM IS VERY BASIC IN THIS PROGRAM WHAT WE ARE DOING IS THAT
#WE ARE USING (AND) LOGICAL OPERTAOR TO COMPARE THE DIFFRENT NUMBERS


#a=int(input("Enter first number: "))
#b=int(input("Enter second number: "))
#c=int(input("Enter thirdnumber: "))
#d=int(input("Enter fourth number: "))
#if(a>b and a>c and a>d):
#    print("greatest number is ",a)
#elif(b>a and b>c and b>d):
#    print("Greates number is",b)
#elif(c>a and c>b and c>d):
#    print("Greates number is",c)
#else:
#    print("greatest number is ",d)
  

#                        #######    METHOD 2      ###########
'''THE LOGIC OF THIS PROGRAM IS THAT WE WILL DIVIDE AND CONQUER  '''
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
num4=int(input("Enter fourth number: "))
if(num1>num2):
    f1=num1
else:
    f1=num2
if(num3>num4):
    f2=num3
else:
    f2=num4
if(f1>f2):
    print(str(f1)+" Is the greatest")
else:
    print(str(f2)+" Is the greatest")