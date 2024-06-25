# to print the only even number multiplication

def display_empty_list(marks,x):
    for item in marks:
        
     res = item*x

    if res % 2 == 0 :
        print(res)
    else:
        print("NO")
        
display_empty_list([1,2,3,4,5,6,7,8,9,10],11)
        
        


        
