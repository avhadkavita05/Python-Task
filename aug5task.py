#Task 1: Accept id card details from console

print("------ID Card------")

name = input("Enter Your Name:")
age = int(input("Enter Your Age;"))
city = input("Enter Your City:")
dob = input("Enter date of birth:")
college = input("Enter your college Name:")
blood_group = input("Enter Blood Group:")

print("\n------MY ID CARD------")
print("Name=",name)
print("Age=",age)
print("City=",city)
print("DOB=",dob)
print("College Name=",college)
print("Blood Group=",blood_group)

#Task 2: Memory Detective
print("\n***Memory Detective***")
v1 = int(input("Enter First Number:"))
v2 = int(input("Enter Second Number: "))
v3 = int(input("Enter Third Number : "))
v4 = int(input("Enter Fourth Number: "))

print("\nMemory Addresses")
print("ID of v1 =", id(v1))
print("ID of v2 =", id(v2))
print("ID of v3 =", id(v3))
print("ID of v4 =", id(v4))

'''----OUTPUT---
PS C:\Users\abc\OneDrive\Desktop\Batch 1341 ws\core python ws> py .\aug5task.py
------ID Card------
Enter Your Name:Kavita Avhad
Enter Your Age;20
Enter Your City:Nashik
Enter date of birth:20-4-2006
Enter your college Name:abc
Enter Blood Group:AB+

------MY ID CARD------
Name= Kavita Avhad
Age= 20
City= Nashik
DOB= 20-4-2006
College Name= abc
Blood Group= AB+

***Memory Detective***
Enter First Number:100
Enter Second Number: 200
Enter Third Number : 400
Enter Fourth Number: 100

Memory Addresses
ID of v1 = 140705358139608
ID of v2 = 140705358142808
ID of v3 = 2983955782864
ID of v4 = 140705358139608
PS C:\Users\abc\OneDrive\Desktop\Batch 1341 ws\core python ws> 
'''