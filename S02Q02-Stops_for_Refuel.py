"""
calculate the number of stops one should make for refuelling 
while travelling from Bangalore to Goa, a distance of 560 kms.
"""

def Vehicle_Mileage():
    start_odometer = float(input("What was first odometer reading? "))
    start_fuel = float(input("How many Litres of fuel had during first odometer reading? "))
    end_odometer = float(input("What was second odometer reading? "))
    fuel_left = float(input("How many litres of fuel left during second odometer reading? "))
    # Calculate Kms driven and fuel used.
    Km_driven = end_odometer - start_odometer
    fuel_used = start_fuel - fuel_left
    # Calculate fuel efficiency and distance left to travel.
    kpl = Km_driven/fuel_used
    return kpl


#Main Starts from here
Target_Dest_Distance=int(input("Enter distance of destination from source: "))
Tank_Capacity=int(input("Enter Car Tank Capacity: "))
Mileage=Vehicle_Mileage()
print ("Vehicle Mileage", Mileage, "Km/L")
#Distance can travel with full capacity
dist_can_travel = Tank_Capacity*Mileage
Num_Refil=0
while dist_can_travel<=Target_Dest_Distance:
    if dist_can_travel < Target_Dest_Distance:
        Target_Dest_Distance=Target_Dest_Distance-dist_can_travel
        Num_Refil+=1
print("Need to stops", Num_Refil, "times for refueling Fuel")

   
    
    






