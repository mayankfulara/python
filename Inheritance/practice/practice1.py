# print a 3d vector using a 2-d vector
class v2d:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
        
    def __str__(self):
        return f"{self.icap}i+{self.jcap}j"


class v3d(v2d):
     def __init__(self, i, j,k):
         super().__init__(i, j) #accessing parents properties
         self.kcap=k
        
     def __str__(self):
        return f"{self.icap}i+{self.jcap}j+{self.kcap}k"


v2=v2d(2,3)
print(v2)
v3=v3d(3,4,5)
print(v3)