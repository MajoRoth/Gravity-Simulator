import turtle
import math

"""
        --- PROGRAM SETTINGS ---
    the lists below contains the specific data of each object
    the lists length can be 2 or 3.
    note that every index corresponds to one object
    e.i. COLOR_LIST[1], MASS_LIST[1], VELOCITY_LIST[1] and POSITION_LIST[1]
    are all attributes of the same object/
"""
COLOR_LIST = ["white", "yellow"]  # list of colors
MASS_LIST = [100, 100]  # list of masses
VELOCITY_LIST = [(0, 1), (0, 0)]  # list of tupels (v_x, v_y)
POSITION_LIST = [(0, 0), (100, 0)]  # list of tupels (x, y)

NUMBER_OF_OBJECTS = len(COLOR_LIST)
G = 2
STROKE = True  # set False if you don't want to see the stroke
ADD_WALLS = False # add walls to prevent objects from leaving
WALL_DAMPING = 0.3  # from 0-1 affects only if PREVENT_EXPLOSION  is True

"""
    --- DATA EXAMPELS ---
    
COLOR_LIST = ["white", "yellow", "green"]  
MASS_LIST = [500, 20, 20]  
VELOCITY_LIST = [(0, 0), (0, 1), (0, -1)]
POSITION_LIST = [(0, 0), (100, 0), (-200, 0)]
NUMBER_OF_OBJECTS = len(COLOR_LIST)
G = 1
STROKE = True
PREVENT_EXPLOSION = False 
WALL_DAMPING = 0.3  

COLOR_LIST = ["white", "yellow"]  # list of colors
MASS_LIST = [10, 20]  # list of masses
VELOCITY_LIST = [(0, 0), (0, 1), ]  # list of tupels (v_x, v_y)
POSITION_LIST = [(0, 0), (100, 0)]  # list of tupels (x, y)
NUMBER_OF_OBJECTS = len(COLOR_LIST)
G = 10
STROKE = True  # set False if you don't want to see the stroke
ADD_WALLS = False # add walls to prevent objects from leaving
WALL_DAMPING = 0.3  # from 0-1 affects only if PREVENT_EXPLOSION  is True

COLOR_LIST = ["white", "yellow"]  # list of colors
MASS_LIST = [10, 10]  # list of masses
VELOCITY_LIST = [(0, -1), (0, 1), ]  # list of tupels (v_x, v_y)
POSITION_LIST = [(100, 100), (0, 0)]  # list of tupels (x, y)
NUMBER_OF_OBJECTS = len(COLOR_LIST)
G = 20
STROKE = True  # set False if you don't want to see the stroke
ADD_WALLS = False # add walls to prevent objects from leaving
WALL_DAMPING = 0.3  # from 0-1 affects only if PREVENT_EXPLOSION  is True
"""

# Screen settings
wn = turtle.Screen()
wn.setup(1200, 800)
wn.screensize(2000, 2000)
wn.bgcolor("black")
wn.title("Gravity Simulator")
wn.tracer(0)


def main():

    # Create objects
    objects = []

    for i in range(NUMBER_OF_OBJECTS):
        objects.append(turtle.Turtle())

    for i in range(NUMBER_OF_OBJECTS):
        objects[i].shape("circle")
        objects[i].color(COLOR_LIST[i])
        objects[i].penup()
        objects[i].speed(0)
        objects[i].mass = MASS_LIST[i]
        objects[i].dx, objects[i].dy = VELOCITY_LIST[i]
        x, y = POSITION_LIST[i]
        objects[i].goto(x, y)

    if STROKE:
        for i in range(NUMBER_OF_OBJECTS):
            objects[i].pendown()

    def gravity_force(obj1, obj2):
        F = G * obj1.mass * obj2.mass / math.pow(obj1.distance(obj2), 2)
        _x1 = obj1.xcor()
        _x2 = obj2.xcor()
        _y1 = obj1.ycor()
        _y2 = obj2.ycor()

        theta = math.atan2(_y1 - _y2, _x1 - _x2)

        Fy = math.sin(theta) * F
        Fx = math.cos(theta) * F

        obj1.dx += (-Fx) / obj1.mass
        obj1.dy += (-Fy) / obj1.mass
        obj2.dx += (Fx) / obj2.mass
        obj2.dy += (Fy) / obj2.mass

    # the main loop
    while True:
        wn.update()
        if NUMBER_OF_OBJECTS == 2:
            gravity_force(objects[0], objects[1])
        elif NUMBER_OF_OBJECTS == 3:
            gravity_force(objects[0], objects[1])
            gravity_force(objects[0], objects[2])
            gravity_force(objects[1], objects[2])

        for obj in objects:
            obj.setx(obj.xcor() + obj.dx)
            obj.sety(obj.ycor() + obj.dy)

            if ADD_WALLS:
                if obj.xcor() > 600 or obj.xcor() < -600:
                    obj.setx(obj.xcor() - obj.dx)
                    obj.dx *= (-WALL_DAMPING)

                if obj.ycor() > 400 or obj.ycor() < -400:
                    obj.sety(obj.ycor() - obj.dy)
                    obj.dy *= (-WALL_DAMPING)


if __name__ == "__main__":
    main()

