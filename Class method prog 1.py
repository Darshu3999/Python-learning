class BookLibrary:
    def __init__(self):
        self.listofBooks = []
    def addBook(self,book):
        self.listofBooks.append(book)
        #print(self.listofBooks)
        #self.showListOfBooks()
    def showListOfBooks(self):
        for b in self.listofBooks:
            print(b)
    
b = BookLibrary()
b.addBook({"id":1,"name":"b1","author":"a1"})
b.addBook({"name":"b1","author":"a1"})
b.addBook({"name":"b1","author":"a1"})
b.addBook({"name":"b1","author":"a1"})
b.showListOfBooks()