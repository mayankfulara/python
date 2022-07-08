def percent(marks):
    p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p
marks1=[78,85,90,92]
percentage1=percent(marks1)
marks2=[90,89,76,100]
percentage2=percent(marks2)
print(percentage1,percentage2)