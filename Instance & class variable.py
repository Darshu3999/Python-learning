class company:
    salary = 100
    def __init__(self,name):
        print("Class Started")
        self.name = name #INSTANCE VARIABLE
        print(self.name)
    def hi(self,msg):
        print("Hi Hello !!",msg)
    def runMsg(self):
        print("Running...")
        
c = company("Darshan") #the constructor is called & its directly executed

c1 = company("Darshan S") #new constructor is called & its directly executed
print(company.salary)
c.runMsg()

#addition using class

class Calculator:
    def __init__(self):
        pass
    
    def addition(self,num1,num2):
        print("The SUM of 2 given numbers is:",num1 + num2)
        
        
    def substraction(self,num1,num2):
        print("The REMAINING of 2 given numbers is:",num1 - num2)
        
    
    def multiplication(self,num1,num2):
        print("The PRODUCT of 2 given numbers is:", num1*num2)
        
        
    def division(self,num1,num2):
        if num2 == 0:
            print("Cannot divide by 0")
        else:
            print("The QUOTIENT of 2 given numbers is:", num1/num2)
 
a1 = Calculator()       
a1.addition(10,20)
a1.substraction(10,5)
a1.multiplication(10,5)
a1.division(10,10)