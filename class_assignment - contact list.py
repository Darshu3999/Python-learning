class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self,contact):
        self.contacts.append(contact)
        print(self.contacts,"added successfully")
        
        
    def display_contacts(self):
        print(self.contacts)
        
    def remove_contact(self):
        for contact in self.contacts:
            if contact["Contact"] == 4456:
                self.contacts.remove(contact)
                print(self.contacts,"removed successfully!")
                
c = ContactList()
c.add_contact({"Name":"Darshan","Contact":8892804259})
c.add_contact({"Name":"Arjun","Contact":123456789})
c.add_contact({"Name":"Rohith","Contact":4456}) 

c.display_contacts()
c.remove_contact()
