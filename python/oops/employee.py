class Employee:
    id:int
    name:str
    gender:str
    department:str
    salary:int

    def create(self,id,name,gender,dept,salary):
        self.id=id
        self.name=name
        self.gender=gender
        self.department=dept
        self.salary=salary

    def get(self):
        print(self.id,self.name,self.gender,self.department,self.salary)

emp1=Employee()
emp1.create(1,"Salman","Male","HR",40000)
emp2=Employee()
emp2.create(2,"Fasil","Male","IT",50000)

emp1.get()
emp2.get()


# self is used to point current object