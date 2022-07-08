                                 #CLASS METHODS

'''IN THIS CODE WE CAN ACCESS THE CLASS DIRECTLY AND NOT ONLY CHANGE THE INSTANCE OF THE CLASS BUT ALSO THE CLASS ITSELF
USING A DECORATER @classmethod'''

class Employee:
    company="Mayank"
    salary="12122"
    
    
    #def changeSalary(self,sal):
    #    self.salary=sal

    @classmethod
    def changeSalary(cls,sal):
        cls.salary=sal
    @classmethod
    def changeCompany(cls,como):
        cls.company=como
E=Employee()
print(E.salary)
print(E.company)
E.changeSalary(12)
E.changeCompany("Fulara")
print(E.company)
print(Employee.company)
print(E.salary)
print(Employee.salary)