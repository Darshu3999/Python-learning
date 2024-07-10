#program to call the function inside the function or inside the class

class Names:
    
    def __init__(self):
        self.listofnames = []
        self.id = 1
        
    def add_names(self,name):
        name.update({"id":self.id})
        self.listofnames.append(name)
        self.id +=1
        return self.listofnames
    
    def remove_names(self,id):
        for index, item in enumerate(self.listofnames):
            if id == item["id"]:
                return index,item,"Removing Name"
                             
    def update_names(self,name,value):
        for item in self.listofnames:
            if name == item["name"]:
                item.update({"name":value})
                return item, "Updated"
            
names = Names()

a = names.add_names({"Name":"Darshan"})
b = names.add_names({"Name":"Ram"})
c = names.add_names({"Name":"Shyam"})
d = names.add_names({"Name":"Raj"})
print(a)
