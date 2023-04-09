from datetime import date
class Student:
    passingpercentage=40
    #instance method 
    def __init__ ( self,name,age,percentage):
        self.__name=name
        self.age=age
        self.percentage=percentage
        
     #will return the object generally factory methods    
    @classmethod
    def  frombirthyear(cls,name,year,percentage):
        return cls(name,date.today().year- year,percentage)
        
    def studentdetails(self):
         print(self.name,self.age,self.percentage)
         
    
    def ispassed(self):
        if Student.passingpercentage<self.percentage:
            print("yes")
        else:
            print("NO")
    
    
    @staticmethod
    def welcometoschool():
        print( "Hey! welcome to school ")
    
    @staticmethod
    def isteen(age):
        return age>16 
s1=Student("vib",22,95)
s2=Student("r1")
s2.frombirthyear("r1",1998,90)
print(s2.__dict__)
s2.studentdetails()
print(s1.isteen(18))
print(s1.__dict__)
   
 #   
        
        