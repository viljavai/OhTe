import turtle
from datetime import datetime
import os
import tkinter as tk

class Plotting:
    """ Visualisaattori 
    """

    def __init__(self, master):
        """ Turtlen alustus 
        """
        self.master = master
        self.canvas = tk.Canvas(self.master)
        self.screen = turtle.TurtleScreen(self.canvas)
        self.turtle = turtle.RawTurtle(self.screen)


    def plot(self,superlist):
        self.canvas.config(width=1500, height=1000)
        self.canvas.pack(side= tk.BOTTOM)
        self.turtle.color("black")
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(-600,-480)
        self.turtle.pendown()
        self.turtle.pensize(1)
        self.turtle.speed(0)
        self.screen.tracer(0,0)
        for jono in superlist:
            self.turtle.penup()
            self.turtle.goto(-500,-480)
            self.turtle.setheading(90)
            self.turtle.pendown()
            for i in range(len(jono)-2,0,-1):
                if jono[i] % 2 == 0:
                    # 10
                    self.turtle.right(int(10))
                    self.turtle.forward(8)
                else:
                    # 18
                    self.turtle.left(int(18))
                    self.turtle.forward(8)
        self.screen.update() 
        turtle.done()

    def save_image(self):
        date = (datetime.now()).strftime("%m.%d.%Y-%H:%M:%S")
        filename = os.environ["HOME"] + "/my_collatz-" + date
        print(filename)
        img = self.turtle.getscreen() 
        img.getcanvas().postscript(file=filename, width=1920, height=1080)
        self.turtle.write("Image saved to home directory!", "right", font=("Verdana", 15, "normal"))
        return filename
