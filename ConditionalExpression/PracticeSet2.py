#TAKE INPUT FROM USER OF THREE SUBJECTS MINIMMUM 40% OVERALL AND MINIMMUM EACH SUBJECT 33%
'''TAKE INPUT OF THREE MARKS'''
a=input("Enter students name: ")
m1=int(input("Enter marks of first subject: "))
m2=int(input("Enter marks of second subject: "))
m3=int(input("Enter marks of third subject: "))
m=m1+m2+m3/3
if(m1<33 or m2<33 or m3<33):
    print(f"{a} your individual marks are less ")
if((m1+m2+m3)/3<40):
    print(f"{a} you fail due to low overall percentge")
else:
    print(f"Congratulations {a} you are pass")
    
