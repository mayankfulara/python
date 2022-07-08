              #CHECKING IF A NAME IS PRESENT IN A LIST OR NOT#
list=['mayank','vatsal','sorav','amitesh','ayush','hema','satish','rajat','shreyansh']
name=input("Enter the name you want to check\n")
if(name in list):
    print(name + "Is part of the family")
else:
    print(name +"Not part of the family")