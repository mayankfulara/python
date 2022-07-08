class Person:
    country="India"
    state="Uttarkhand"

    def __init__(self):
        print("Initialising Person.....")


    def takeBreath(self):
        print("I am breathing")

class Employee(Person):
    company="Google"


    
    def __init__(self):
        super().__init__()
        print("Initialising Employee.....")

    def takeBreath(self):
        super().takeBreath()
        print("i am an Employee and brathing........")


class intern(Employee):
    name="Mayank"
    def __init__(self):
        super().__init__()
        print("Initialising Programmer.....")
    def takeBreath(self):
        super().takeBreath()
        print("I am a intern and still breathing.....")

#p=Person()
#p.takeBreath()

#e=Employee()
#e.takeBreath()

i=intern()
#i.takeBreath()