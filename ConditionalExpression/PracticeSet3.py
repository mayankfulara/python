a=input("Enter message: ")
if("make lot of money" in a):
    spam=True
elif("buy now " in a):
    spam=True
elif("subscribe this"in a):
    spam=True
elif("click this"in a):
    spam=True
else:
    spam=False
if(spam):
    print("This message is  a spam")
else:
    print("Yor message is: "+a)