'''ICE CREAM PROBLEM'''

import math
def quantityoficeream(r,h):
    c=(((2*r)+h)*r*r)
    return c
r=int(input("Radius: "))
h=int(input("Height: "))
qoc=quantityoficeream(r,h)
print(qoc)