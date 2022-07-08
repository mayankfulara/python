import random
class Employee:
    copany="Visa"
    ecode=23
    


class Freelancer:
    company="Fiverr"
    ceo="Mayank"
    level=random.randint(4,8)
    print(level)
    

    def uplevel(self):
        self.level=self.level+random.randint(1,4)
        print(f"The level is {self.level}")
        if self.level>6:
            print(" addvance programmer")
        elif 3<self.level>6:
            print("Intermediate programmer")
        else:
            print("Beginer programmer")


class Programmer(Employee,Freelancer):
    name="Mayank"

p=Programmer()
p.uplevel()
print(p.company)
print(p.ceo)

