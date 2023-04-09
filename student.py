class Student:
    passingpercentage=40
    #instance method 
    def __init__ ( self,name,age,percentage):
        self.name=name
        self.age=age
        self.percentage=percentage
        
        
        
    def studentdetails(self):
        self.name="vib"
        self.age=22
        #percentage=88 can be accessed locally only 
        self.percentage=90 #now it can accessed as it is a instance attribute 
        print(self.name)
        print(self.percentage)

        
        # print(percentage)
    
    def ispassed(self):
        if Student.passingpercentage<self.percentage:
            print("yes")
        else:
            print("NO")
    # for static method  use Decroator  # if required without self and to  avoid this error  welcometoschool() takes 0 positional arguments but 1 was given
    
    @staticmethod
    def welcometoschool():
        print( "Hey! welcome to school ")
        
        
    


s1=Student()
print(s1)
# print(s1.studentdetails(). 
s1.studentdetails()
s1.ispassed()
s1.welcometoschool()




        