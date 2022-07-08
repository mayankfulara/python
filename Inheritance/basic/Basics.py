class Employee:
    company="Google"

    def Showdetails(self):
        print(f"This is an employee of {self.company}")

class Programmer(Employee):
     #company="Youtube"
     lang="python"
     def Showlang(self):
         print(f"Language is {self.lang} and company is {self.company}")

e=Employee()
e.Showdetails()
p=Programmer()
p.Showlang()
