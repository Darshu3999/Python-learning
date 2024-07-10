#calling the function in different class or function

class Animals():
    
    
    def __init__(self):
        
        self.animals = []
        self.id = 1
        
    def dog(self,animal):
        animal.update({"id":self.id})
        self.animals.append(animal)
        self.id += 1
        print(self.animals,"New DOG Added To The List !!")
        
    def cat(self,animal):
        animal.update({"id":self.id})
        self.animals.append(animal)
        self.id +=1
        print(self.animals,"New CAT Added To The List !!")
        
    def remove_dog(self,id):
        for index, item in enumerate(self.animals):
            if item["id"] == id:
                print(index,item,"Sucessfully removed from the DOG List")
                self.animals.pop(index)
                
    def remove_cat(self,id):
        for index, item in enumerate(self.animals):
            if item["id"] == id:
                print(index,item,"Sucessfully removed from the CAT List")
                self.animals.pop(index)
        
        
               
animal = Animals()
animal.dog({"speak":"woof","name":"Chintu","age":3})
animal.dog({"speak":"woof","name":"Monu","age":2})
animal.cat({"speak":"meaow","name":"prino","age":2})
animal.cat({"speak":"meaow","name":"princy","age":1})

animal.remove_dog(2)
animal.remove_cat(1)

