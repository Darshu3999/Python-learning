list = [1,2,3,4,5,6]
list.append(10)
print("New number 10 is added to the list",list)
list.pop(1)
print("1st indexed is poped out of the list",list)
list.insert(5,20)
print("new item is added to the list at 5th index",list)


#using for loop

for item in list:
    if len(list) == 7:
        list.append(55)
        print(item)
    else:
        print(item)
        
             
#removing 

n = [8,9,3,1,2,0,5,0]


#using loop
for item in n:
    if item != 0:
       print(item)

