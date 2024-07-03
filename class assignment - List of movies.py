class Movielist:
    def __init__(self):
        self.movie = []

    def add_movie(self,movie):
        self.movie.append(movie)
        print(self.movie,"added successfully!")
        
        
    def remove_movie(self,Year):
        for index,item in enumerate(self.movie):
            if Year == item['Year']:
                print(index,item)
                self.movie.pop(index)
    
    def particular_movie(self, Year):
        for index,item in enumerate(self.movie):
            if Year == item['Year']:
                print(index,item['Movie_Name'])
                
    def display_movie(self):
        print(self.movie)
            
                
    
c = Movielist()
c.add_movie({"Movie_Name":"MAJESTIC","Year":1999})
c.add_movie({"Movie_Name":"SHOURYA","Year":2010})
c.add_movie({"Movie_Name":"DASA","Year":2000})
c.add_movie({"Movie_Name":"VIRAT","Year":2016})

c.remove_movie(2000)
c.display_movie()
c.particular_movie(1999)
