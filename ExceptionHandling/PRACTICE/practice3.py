#MULTIPLICATION TABLE OF THE USER ENTERED NUMBER

num=int(input("Enter the number: "))
table=[num*i for i in range(1,11)]
print(table)