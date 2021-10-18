import math
import random

class Human():
    def __init__(self, age=None, gender=None):
        if age is not None:
            self.age = age
        else:
            self.age = random.randint(0,160)
            random.ran
        if gender is not None:
            self.gender = gender
        else:
            self.gender = random.choice(["male","female"])

    @property
    def age(self):
        return self.age

    @property
    def gender(self):
        return self.gender                        

    @classmethod
    def eat(cls,eat):
        cls.eat = eat
    
    def sleep(cls,sleep):
        cls.sleep = sleep 

    def run(cls,run):
        cls.run = run       

class studen(Human):
    def __init__(self, age=None, gender=None, id=None, credit=None, grade=None):
        super().__init__(age, gender)
        if age is not None:
            self.age = age
        else:
            self.age = random.randint(18, 28)
        self.complex_list = []
        if id is not None:
            self.id = id
        else:
            self.id = random.randint(0,9999)
        if credit is not None:
            self.credit = credit
        else:
            self.credit = random.randint(0,250)
        if grade is not None:
            self.grade = grade
        else:
            self.grade = round(random.uniform(0,4.0),1)

    @property
    def age(self):
        return self.age
    @property
    def id(self):
        return self.id
    @property
    def grade(self):
        return self.grade
    @property
    def credit(self):
        return self.credit

    def result(self):
        if (self.grade>=3.8)and(self.grade<=4.0):
            return self.result=="A+"
        elif (self.grade>=3.3)and(self.grade<=3.5):
            return self.result=="A"
        elif (self.grade>=3.0)and(self.grade<=3.2):
            return self.result=="B+"
        elif (self.grade>=2.6)and(self.grade<=2.9):
            return self.result=="B"
        elif (self.grade>=1.8)and(self.grade<=2.5):
            return self.result=="C"
        else:
             return self.result=="D"                         

    def graduate(self):
        if (self.result != "D") and (self.credit == 250) :
            return True
        else:
            return False    





                    
          
        