class Student:
    passingpercentage=35
    def __init__ ( self,name,age,percentage):
        self.__name=name
        self.age=age
        self.percentage=percentage
    def __ispassed(self):
        if Student.passingpercentage<self.percentage:
            print("yes")
        else:
            print("NO")
        
    
        
s1=Student("ritik",23,55)

#AttributeError: 'Student' object has no attribute 'name' it cannot be accessed outside the clas 

print(s1._Student__name)#or using  name mangling 

s1.ispassed()
# print(s1.name)

