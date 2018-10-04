'''
Get the user’s first name and last name. 
        Assume the user provides “Dharmender” and “Singh” as inputs, 
        Find his best possible initials by eliminating the last character 
        from each of the name as shown in this sample output        - Step 1 : Dharmender Singh
        - Step 2 : Dharmende Sing
        - Step 3 : Dharmend Sin
        - Step 4 : Dharmen Si
        - Step 5 : Dharme S

        Expected output :
        Best possible initials of "Dharmender Singh" is :
        Dharme S
'''

#Main Starts from here
first_name = input("Please enter First name:")
last_name  = input("Please enter last name:")

print("Entered Name:",first_name,last_name,"\n")

for i in range(1, len(last_name)):
    first_name = first_name[:-1]
    last_name  = last_name[:-1]
    print("Step"+str(i),first_name,last_name)

print(f"Best possible initials of \"Dharmender Singh\" is :\n{first_name} {last_name}")
