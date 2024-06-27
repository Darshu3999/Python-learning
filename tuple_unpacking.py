#tuple unpacking & adding of those numbers

my_tuple = (10,20,30,9)
my_list = [10,50,60]
my_list.append(20)
my_list1 = my_list

def addition(my_tuple):
    a,b,c,d = my_tuple
    num = a+b+c+d
    print(num)

addition(my_tuple)
addition(my_list1)

#to calculate the intrest

principle = int(input("Enter the principle amount:"))
time = int(input("Enter the time given:"))
rate = int(input("Enter the rate of intrest:"))

def simple_intrest(principle,time,rate):
    si = (principle*time*rate)/100
    print(si)
simple_intrest(principle,time,rate)

#calculator

def calculator():
    print("Enter the operation you want to perform:")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print("Enter the numbers you want to add:")
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        print("The sum of the numbers is:",num1+num2)
    elif choice == 2:
        print("Enter the numbers you want to subtract:")
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        print("The difference of the numbers is:",num1-num2)
    elif choice == 3:
        print("Enter the numbers you want to multiply:")
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        print("The product of the numbers is:",num1*num2)
    elif choice == 4:
        print("Enter the numbers you want to divide:")
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        if num2 == 0:
            print("Cannot divide by zero")
        print("The quotient of the numbers is:",num1/num2)
calculator()
        