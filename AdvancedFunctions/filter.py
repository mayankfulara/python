# FILTER OUT THE LIST
l=[2,3,4,5,6,7,87,7,55]
def graeter_than_5(num):
    if num>5:
        return True
    else:
        return False

g10= lambda num:num>10

print(list(filter(graeter_than_5,l)))
print(list(filter(g10,l)))
