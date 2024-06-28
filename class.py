class myself:
    def __init__(self,name,age):
        print("Hi")
        self.name = name
        self.age = age
        
        
    def myself_1(self,email):
        self.email = email

        
    def addition(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        return self.num1 + self.num2
    
    def substraction(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        return self.num1 - self.num2
    
    def multiplication(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        return self.num1 * self.num2
    
    def division(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        if self.num2 == 0:
            print("cannot be divided bt zero")
        else:
            return self.num1 / self.num2

        
my=myself("dacchu",25) 
print(my.name)      
print(my.age)
my.myself_1("darsh@gmail.com")
print(my.email)
print("************ END ************")

print(my.addition(50,20))
print(my.substraction(50,20))
print(my.multiplication(5,2))
print(my.division(5,0))
