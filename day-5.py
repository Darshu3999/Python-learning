n = [8,9,3,1,2,0,5,0]
print("Old list with out updation:", n)
m=[]
for item in n :
    m.append(item)
print("New list with updation:", m)
m.append(25)
print("Output after Appending 25:", m)
m.insert(8,20)
print("Output after inserting 20:", m)

#zero's & number's in different list


zeros=[]
numbers=[]
for item in n:
    if item == 0:
        zeros.append(item)
    else :
        numbers.append(item)
print(zeros)
print(numbers)

