n=int(input("Enter the number you want to check: "))
if(n%2!=0):
    print("Weird")
elif(n%2==0 and 2<n<5 ):
    print("Not weird")
elif(n%2==0 and 6<n<20):
    print("Not Weird")
else:
    print("Not Weird")
    