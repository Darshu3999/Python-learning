class company:
    def __init__(self):
        print("Class Started")
    def hi(self,msg):
        print("Hi Hello !!",msg)
        
c = company() #the constructor is called & its directly executed
c.hi("Hello") 
c1 = company() #new constructor is called & its directly executed
c.hi("Hi")
c1.hi("Hello")