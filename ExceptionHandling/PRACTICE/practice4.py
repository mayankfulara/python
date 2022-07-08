#DO A/B AND IF B=0 HANDLE THAT ERROR
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
try:
    c=a/b
    print(c)

except ZeroDivisionError as e:
    print("Infinite") 