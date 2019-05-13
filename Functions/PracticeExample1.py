"""
Write a function that computes the volume of a sphere given its radius.
volume=4/3pir3
"""
import math

def volume_of_sphere(radius):
    volume=(4/3)*math.pi*radius**3
    print('Volume of the Sphere is ',volume)

volume_of_sphere(2)
