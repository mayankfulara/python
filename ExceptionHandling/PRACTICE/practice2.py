# WE HAVE TO PRINT THE FIFTH SIXTH SEVENTH ELEMENT OF THE LIST USING ENUMERATE FUNCTION

A=[1,2,3,4,5,6,7,8,9]
for i,item in enumerate(A):
    if i==5 or i==6 or i==7:
        print(f"The element at index {i} is: {item}") 