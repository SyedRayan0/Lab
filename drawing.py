'''This module contains the main function which runs the relevant function imported from the Pixart module
'''
import turtle
from pixart import draw_shape_from_file

def main():
    screen = turtle.Screen()  # Create a screen
    screen.bgcolor("skyblue")
    
    turta = turtle.Turtle()  # Create a turtle object
    turta.speed(0)
    turta.penup()
    turta.goto(-200,200)
    turta.pendown()

    draw_shape_from_file(turta)

    input("Press enter to exit..")

if __name__ == "__main__": # To control the execution of code within this script
    main()