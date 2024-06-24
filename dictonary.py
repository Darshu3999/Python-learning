emp = {"name":"abcd","id":1}
empList = [{"name":"abcd","id":1},{"name":"xyz","id":2}]
for item in empList:
    print('name',item['name'],'id',item['id'])
    

#def function

def display_emp_list():
    emp = {"name":"abcd","id":1}
    empList = [{"name":"abcd","id":1},{"name":"xyz","id":2}]
    for item in empList:
        print('name',item['name'],'id',item['id'])
display_emp_list()


def display_emp_list(marks):
   print(marks)
   for item in marks:
       res = item
       print(item)
display_emp_list([1,2,3,4])

x =10
if x ==10:
    print("yes")
else:
    print("no")
    