class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __add__(self,other):
        if isinstance(other,Employee):
            return Employee(self.name+" & "+other.name,self.salary+other.salary)
        return None
    def __sub__(self,other):
        if isinstance(other,Employee):
            return abs(self.salary-other.salary)
        return None
    def __lt__(self,other):
        return self.salary<other.salary if isinstance(other,Employee) else False
    def __le__(self,other):
        return self.salary<=other.salary if isinstance(other,Employee) else False
    def __gt__(self,other):
        return self.salary>other.salary if isinstance(other,Employee) else False
    def __ge__(self,other):
        return self.salary>=other.salary if isinstance(other,Employee) else False
    def __eq__(self,other):
        return self.salary==other.salary if isinstance(other,Employee) else False
    def __ne__(self, other):
        return self.salary!=other.salary if isinstance(other,Employee) else True
    def display(self):
        print(f"Employee Name: {self.name}, Salary: ${self.salary}")
def main():
    name1=input("Enter first employee's name: ")
    salary1=float(input("Enter first employee's salary: "))
    emp1=Employee(name1, salary1)
    
    name2=input("Enter second employee's name: ")
    salary2=float(input("Enter second employee's salary: "))
    emp2=Employee(name2, salary2)
    emp3=emp1+emp2
    if emp3:
        print("Combined Employee:")
        emp3.display()
    else:
        print("Invalid operation.")
    salary_difference=emp1-emp2
    if salary_difference is not None:
        print(f"Salary difference: ${salary_difference}")
    else:
        print("Invalid operation.")
    print(f"{emp1.name} earns less than {emp2.name}:", emp1 < emp2)
    print(f"{emp1.name} earns more than {emp2.name}:", emp1 > emp2)
if __name__ == "__main__":
    main()