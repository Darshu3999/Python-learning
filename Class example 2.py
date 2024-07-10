#calling the function in different class or function
class vote():
    def __init__(self):
        self.title = "Hello Voter"
        self.votecount = 0
        self.voter_list = []
        self.nonvoter_list = []
    
    def allow_voting(self,voter):
        print(self.title)
        self.duplicate_voters(voter['id'])
        result = self.check_eligibility(voter['age'])
        if result == True:
            print ("You are ELIGIBLE TO VOTE")
            self.votecount = self.votecount+1
            self.voter_list.append(voter)
            print(self.voter_list, "Voter List is updated !!")
            print("Total Votes :",self.votecount,"Voters Only")
        else:
            print ("You are NOT ELIGIBLE TO VOTE")
            self.nonvoter_list.append(voter)
            print(self.nonvoter_list, "Non Voter List is updated !!")
            
    def duplicate_voters(self,id):
        for item in self.voter_list:
            if id == item["id"]:
                print("Duplicate Voter Found !!")
            else:
                return True
            
    def check_eligibility(self,age):
        if age >= 18:
            return True
        else:
            return False
            
v = vote()
v.allow_voting({"Name":"Darshan","age":20,"id":1})
v.allow_voting({"Name":"Rajesh","age":25,"id":2})
v.allow_voting({"Name":"Bheema","age":30,"id":3})
v.allow_voting({"Name":"Bheema","age":30,"id":3})
v.allow_voting({"Name":"Sreenu","age":32,"id":4})
v.allow_voting({"Name":"Lohith","age":16,"id":5})
v.allow_voting({"Name":"Ram","age":17,"id":6})
            
        
        