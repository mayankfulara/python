#LIST COMPREHENSION CAN EB USED TO CREATE LISTS
a=[34,65,3,7,8,9,24,2,5]
#b=[]
#for i in a:
#    if i%2==0:
#        b.append(i)
#        b.sort()
b=[i for i in a if i%2==0]
b.sort()
print(b)

t=[1,2,3,4,4,3,2,1]
s={i for i in t}
print(s)