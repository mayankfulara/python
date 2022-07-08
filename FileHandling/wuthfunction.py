#THIS FUNCTIOIN OPENS THE FILE WITHOUT HAVING THE NEED TO CLOSE IT
with open("another.txt",'r')as f:
    a=f.read()
print(a)