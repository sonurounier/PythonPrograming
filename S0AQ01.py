'''
A melting furnace converts a hollow sphere into a solid cylinder of 3cm diameter with a 5% loss. 
Write a program that finds out the length of the solid cylinder when
 the inner and external radii of the hollow sphere are known
Volume of sphere = 4/3 * pi * r * r * r
Volume of cylinder = pi * r * r * height
'''

from math import pi

def vol_sphere(radius):
    volume = 4/3*pi*(radius ** 3)
    return volume
 
def main():
    cyl_radius = 1.5
    ext_radius_sp = 5
    int_radius_sp = 3
    vol_hollow_sphere = vol_sphere(ext_radius_sp) - vol_sphere(int_radius_sp)

    vol_after_5cent_loss = vol_hollow_sphere - (5/100*vol_hollow_sphere)
    vol_cyl = vol_after_5cent_loss
    cyl_height = vol_cyl/(pi*cyl_radius*cyl_radius)

    print (f"Volume of sphere before melting is :{vol_hollow_sphere:.2f} cubic cm\n")
    print(f"5% loss of sphere after melting is: {(5/100*vol_hollow_sphere):.2f} cubic cm\n")
    print(f"Volume of Sphere which is equal to Cylinder is: {vol_after_5cent_loss:.2f} cubic cm\n" )
    print(f"Height of Cylinder is: {cyl_height:.2f} cm\n" )
 
main()
