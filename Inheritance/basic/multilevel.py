class Person:
    country="India"
    state="Uttarkhand"

class Employee(Person):
    company="Google"

    def takeBreath(self):
        print("i am an Employee and brathing........")


class intern(Employee):
    name="Mayank"
    #def takeBreath(self):
        #print("I am a intern and still breathing.....")
i=intern()
print(i.country)
i.takeBreath()
print(i.company)
print(i.name)