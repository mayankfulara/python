'''We need to find the greatest of three usimg functions'''


def greatest(num1,num2,num3):
    if (num1 > num2 ):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3


n1 = int(input("Enter the first number: \n"))
n2 = int(input("Enter the second number: \n"))
n3 = int(input("Enter the third number: \n"))
m=greatest(n1,n2,n3)
print("Gratest number is ",m)