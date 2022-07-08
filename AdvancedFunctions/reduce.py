# REDUCE FUNCTION
'''SO WHAT A REDUCE FUNCTION DOES IS IT APPLIES ROLLING COMPUTATION TO THE SEQUENTIAL PAIR OF ELEMENTS'''

from functools import reduce
sum=lambda a,b:a-b
l=[1,3,4,5]
val=reduce(sum,l)
print(val)