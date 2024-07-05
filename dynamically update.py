emp = {"Employee_1":"Darshan","ID_1": 6106,"Employee_2":"PAVITRA","ID_2": 6204}
print(emp, "NOT UPDATED EMPLOYEE LIST.")

Unique_key = int(input("Enter the Employee_ID: "))
value = input("Enter the Employee Name to be UPADTED: ")

emp.update({Unique_key:value}) 
print(emp,"UPDATED EMPLOYEE LIST.")