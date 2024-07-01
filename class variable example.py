class Library:
    
    def __init__(self):
        self.booksList = []
        
    def add_book(self,book):
        self.booksList.append(book)
        print(book)
    
    def remove_book(self,book):
        print(book)
        
        
a = Library()
a.add_book({"Book_No": 1,"Author":"APJ ABDUL KALAM","Book_Name_1":"AGNI KI UDAAN"})
a.add_book({"Book_No": 2,"Author":"J K Rooling","Book_Name_2":"Harry Potter"})
        
 
        

    