name = "Darshan S"
print("output for VARIABLES:",name)

list_1 = [0,1,2,'Darshan']
print("output for LIST: ",list_1)

dict = {"name":"Darshan S", "ph_no":1234}
print("output for the DICTONARY_name:",dict['name'])
print("output for the DICTONARY_ph_no:",dict['ph_no'])

myset = {1,2,3,5,10}

for item in myset:
    print("The output for the set using FOR LOOP:", item)
    
my_tuple = (1,2,3,4,5)
my_tuple_1 = list(my_tuple)
my_tuple_1.append(0)
print("The output for tuple: ", my_tuple_1)

def multiplication(a,b):
    return a*b
print("The output for the FUNCTION:",multiplication(5,6))

num = int(input("Enter the NUMBER to know whether its EVEN OR ODD: "))

if num%2 ==0:
    print("The number is EVEN")
else:
    print("The number is ODD")


