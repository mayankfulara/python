class Number:
    def __init__(self,num1):
        self.num=num1
    def __add__(self,num2):
        print("Add")
        return self.num+num2.num
    def __mul__(self,num2):
        return self.num*num2.num
    def __sub__(self,num2):
        return self.num-num2.num

n1=Number(4)
n2=Number(6)
sum=n1+n2 
mul=n1*n2 
sub=n1-n2 
print(mul)     
print(sum)     
print(sub)