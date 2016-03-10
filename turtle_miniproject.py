# turtle_miniproject
# Udacity / Programming Foundations with Python / Lesson 2A
# Creates a specific image for a class project

import turtle

# The size of triangle sides
side = 50

def draw_triangle(some_turtle):

    # Draws triangle
    some_turtle.begin_fill()
    for i in range (1,4):
        some_turtle.forward(side)
        some_turtle.left(120)
    some_turtle.end_fill()  
        
def draw_art():

    # Creates the screen for drawing
    window = turtle.Screen()
    window.bgcolor("white")
    
    # Creates link the turtle
    link = turtle.Turtle()
    link.shape("turtle")
    link.color("blue", "green")
    link.speed(6)
    start = link.position()

    # Creates bottom row of triangles
    for i in range (1,9):
        draw_triangle(link)
        link.forward(side)
        if i is 8:
            end = link.position()

    # Returns to the starting position
    link.goto(end)
    link.goto(start)
    link.left(60)
    link.forward(side)
    link.right(60)

    # While loop will draw trianlges differnt colors based on rows
    # Blank spaces are drawn as white triangles using if statements nested in the for
    # Turtle always returns to its original position after drawing the row of triangles
    # z is used to move the turtle to the next row and v is to identify which row
    z = 2
    v = 8
    while v>1:
        link.color("blue", "green")
        if v is 8:
            for i in range (1,v):
                link.color("blue", "green")
                if (i is 2) or (i is 4) or (i is 6):
                    link.color("white", "white")   
                draw_triangle(link)
                link.forward(side)
        if v is 7:
            for i in range (1,v):
                link.color("blue", "green")
                if (i is 3) or (i is 4):
                    link.color("white", "white")   
                draw_triangle(link)
                link.forward(side)
        if v is 6:
            for i in range (1,v):
                link.color("blue", "green")
                if (i is 2) or (i is 3) or (i is 4):
                    link.color("white", "white")   
                draw_triangle(link)
                link.forward(side)
        if v is 5:
            for i in range (1,v):
                link.color("blue", "green")  
                draw_triangle(link)
                link.forward(side)
        if v is 4:
            for i in range (1,v):
                link.color("blue", "green")
                if (i is 2):
                    link.color("white", "white")   
                draw_triangle(link)
                link.forward(side)
        if v is 3:
            for i in range (1,v):
                link.color("blue", "green")  
                draw_triangle(link)
                link.forward(side)
        if v is 2:
            for i in range (1,v):
                link.color("blue", "green") 
                draw_triangle(link)
                link.forward(side)
                
        # Returns to the starting position        
        link.goto(end)
        link.goto(start)
        link.left(60)
        link.forward(side*z)
        link.right(60)
        
        # Increments counters
        z = z + 1
        v = v -1

    window.exitonclick()

draw_art()
