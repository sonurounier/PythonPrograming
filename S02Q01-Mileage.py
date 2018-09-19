"""
Using the starting and ending values of your car’s odometer, 
            calculate its mileage
"""

start_odometer = float(input("What is the first odometer reading?\n"))
start_fuel_cap = float(input("How many Litres of fuel does your tank have\n"))
end_odometer = float(input("What is next odometer reading?\n"))
fuel_left = float(input("How many litres of fuel were left?\n"))

# Calculate Kms driven and fuel used.
Km_driven = end_odometer - start_odometer
fuel_used = start_fuel_cap - fuel_left
# Calculate fuel efficiency and distance left to travel.
kpl = Km_driven/fuel_used
print("Mileage of vehicle is", kpl,"Km/ltr")
distance_left = fuel_left*kpl
print("You can go",distance_left,"Km before refuel.")
