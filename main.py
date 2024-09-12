class Person: 
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def prname(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year
 
S = Student("Anurag", "Dey", "2009")
S.prname()
print(S.year)