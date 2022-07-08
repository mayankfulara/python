def multiply_two_strings(a,b):
   # code here
   # return the product string
   product = int(a) * int(b)
   return(product)


t=int(input('Enter the number of pairs to be multiplied: '))
for i in range(t):
   a,b=input('Enter a pair: ').split()
   print(multiply_two_strings( a.strip() , b.strip() ))
