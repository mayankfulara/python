# THE PROBLEM IS TO EXTERACT THE NUMBERS DIVISIBLE BY 5 FROM THE LIST

a=[2,3,4,5,10,20,25]
#def test(num):
#    if num%5==0:
#        return True
#    else:
#        return False
#print(list(filter(test,a)))

'''METHOD 2'''
k=filter(lambda a: a%5==0,a)
print(list(k))