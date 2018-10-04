'''
Get the user's first name and last name.
Assume the user provides "Dharmender" and "Singh" as inputs
then print the user's name in the following order and format

-Name: dharmender, Surname: singh
-DHARMENDER SINGH
 ---------- -----
-Dharmender, Singh
'''

#Main Starts from here
first_name = input("Please enter First name:")
last_name  = input("Please enter last name:")

first_name_uline = "-" * len(first_name)
last_name_uline  = "-" * len(last_name)

print("\nName:",first_name.lower(),", Surname:",last_name.lower(),"\n")

print(first_name.upper(),last_name.upper())
print(first_name_uline,last_name_uline,"\n")

print(first_name,",",last_name)


