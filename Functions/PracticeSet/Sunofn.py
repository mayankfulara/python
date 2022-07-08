def sumof(n):
    if n==0 or n==1:
        return 1
    return n+sumof(n-1)
num=int(input("Enter the limit: "))
m=sumof(num)
print("The sum of numbers is ",m)