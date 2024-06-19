#to eliminate the duplicate numbers inthe guven list

list=[1,3,6,6,7,10,10,1]
new_list=[]

for item in list:
    if item not in new_list:
        new_list.append(item)
        
print("Old list with out removing duplicate numbers:", list)
print("New List after removing the duplicate numbers", new_list)