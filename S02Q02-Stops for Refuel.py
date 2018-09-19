"""
calculate the number of stops one should make for refuelling 
while travelling from Bangalore to Goa, a distance of 560 kms.
"""

#Main Starts from here

Target_Dest_Distance=int(input("Enter distance of destination from source: "))

Tank_Capacity=int(input("Enter Car Tank Capacity: "))

Mileage=int(input("Enter Vehicle Mileage: "))

#Distance can travel with left fuel in vehicle
dist_can_travel = Tank_Capacity*Mileage
print("You can go",dist_can_travel,"Km before refuel.")

Num_Refil=0
while dist_can_travel<=Target_Dest_Distance:
    if dist_can_travel < Target_Dest_Distance:
        Target_Dest_Distance=Target_Dest_Distance-dist_can_travel
        Num_Refil+=1
print("Need to stops", Num_Refil, "times for refueling Fuel")

   
    
    






