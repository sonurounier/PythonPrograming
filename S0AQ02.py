'''
Like everyone I too enjoyed watching Taj Hotel from Mumbai’s Gateway of India. 
When I stood at the Gateway of India, I saw that the 
top of Taj Hotel’s tower was at an angle of elevation of 25 degrees.
I then walked to the security guard near the gate of Taj Hotel and 
noticed that the top of the tower was at an angle of elevation of 65 degrees. 
The security guard informed me that the Tower was about 100 yards from the gate.Write a program to find the height of Taj Hotel’s tower and 
the distance between Gateway of India and Taj Hotel’s entrance.
'''

from math import tan, radians
content='''
    |\\-->65 degree
    | \\
    |  \\
ht  |   \\   tan65= ht/base
    |    \\
    |     \\
    |      \\ --->100 yards from tower
    ---------
    base'''

print(content)

distance  = float(input("Enter distance of tower from gate:\n"))
elevation = float(input("Enter angel of elevation to top of tower from gate:\n"))

in_radian = radians(elevation) #need to convert from degree to radian as tan input is radian

tower_height = tan(in_radian) * distance

print("Heigt of Tower is:",tower_height, "yards")




