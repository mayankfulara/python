#PROBLEM IS TO FIND THE MINIMMUM OF THE LIST USING REDUCE FUNCTION

from functools import reduce
a=[2,4,5,6,7,5,2,2]
b=reduce(min,a)
x=reduce(max,a)
print("Minimmum number is:",b)
print("Maximum number is:",x)

