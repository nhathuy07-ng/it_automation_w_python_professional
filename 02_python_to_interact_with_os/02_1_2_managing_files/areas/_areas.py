import math

def triangle(base: float, height: float) -> float:
    return base*height/2

def rectangle(base: float, height: float) -> float:
    return base*height

def circle(radius: float) -> float:
    return math.pi * (radius ** 2)

def donut(outside_radius: float, inside_radius: float) -> float:
    return circle(outside_radius) - circle(inside_radius)
