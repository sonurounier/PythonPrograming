"""
Using the starting and ending values of your car’s odometer, 
            calculate its mileage
"""
def sub(num1, num2):
    diff=float(num1-num2)
    return diff

def divide(num1, num2):
    division=float(num1/num2)
    return division

def multiplication(num1, num2):
    product=float(num1*num2)
    return product

#Main Starts from here
start_odometer = float(input("What is the first odometer reading?\n"))
start_fuel_cap = float(input("Litres of fuel had during first odometer reading\n"))
end_odometer = float(input("What is next odometer reading?\n"))
fuel_left = float(input("How many litres of fuel were left?\n"))

# Calculate Kms driven and fuel used.
Km_driven = sub(end_odometer,start_odometer)
fuel_used = sub(start_fuel_cap, fuel_left)
# Calculate fuel efficiency and distance left to travel.
kpl = divide(Km_driven, fuel_used)
print("Mileage of vehicle is", kpl,"Km/ltr")
distance_left = multiplication(fuel_left, kpl)
print("You can go",distance_left,"Km before refuel.")
