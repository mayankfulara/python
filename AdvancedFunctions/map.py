# SO WE NEED TO SQUARE  THE NUMBERS PRESENT IN THE LIST
'''THERE ARE TWO METHODS OF DOING THE TASK'''
'''FIRST IS USING THE FOR LOOP AND THE SECOND IS USING THE MAP FUNCTION'''
#SO MAP FUNCTION IS USED TO 
''' APPLY THE FUNCTION TO ALL THE ITEMS PRESENT IN THE LISTn''' 


# square=lambda a:a*a
def square(a):
    return a*a
# METHOD 1
l=[2,4,6]
l1=[]
for item in l:
    l1.append(square(item))
print(l1)


#METHOD 2
print(list(map(square,l)))


