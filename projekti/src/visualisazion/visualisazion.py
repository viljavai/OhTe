import turtle
from datetime import datetime
import os
import tkinter as tk

class Plotting:
    """Luodaan kuvaaja
    """

    def __init__(self, master, canvas):
        """alustetaan turtle-olio

        Args:
            master: tkinter-olio, jolla yhdistetään GUI ja turtle-ruutu
        """
        self.canvas = canvas
        self.master = master
        self.screen = turtle.TurtleScreen(self.canvas)
        self.turtle = turtle.RawTurtle(self.screen)


    def plot(self,superlist, angle, numvar):
        """Kuvaajan luonnin logiikka

        Args:
            superlist: Lukujonot välillä (integer,..1)
            angle: käyttäjäsyöte
            numvar: Boolean
        """
        self.canvas.config(width=1920, height=1200)
        self.canvas.pack(side=tk.BOTTOM)
        self.turtle.color("black")
        self.turtle.hideturtle()
        self.turtle.penup()
        if angle > 15:
            self.turtle.goto(-400,-400)
        else:
            self.turtle.goto(-400,-550)
        self.turtle.pendown()
        self.turtle.pensize(1)
        self.turtle.speed(0)
        self.screen.tracer(0,0)
        for jono in superlist:
            if numvar is True:
                self.turtle.write(jono[0], "right", font=("Verdana", 5, "normal"))
            self.turtle.penup()
            if angle >= 15:
                self.turtle.goto(-400,-400)
            else:
                self.turtle.goto(-400,-550)
            self.turtle.setheading(90)
            self.turtle.pendown()
            for i in range(len(jono)-2,0,-1):
                if jono[i] % 2 == 0:
                    # 10
                    self.turtle.right(int(angle))
                    self.turtle.forward(6)
                else:
                    # 18
                    self.turtle.left(int(angle*1.8))
                    self.turtle.forward(6)
        self.screen.update()

    def save_image(self):
        date = (datetime.now()).strftime("%m.%d.%Y-%H:%M:%S")
        filename = os.environ["HOME"] + "/my_collatz-" + date
        print(filename)
        img = self.turtle.getscreen()
        img.getcanvas().postscript(file=filename, width=1920, height=1200)
        self.turtle.write("Image saved to home directory!", "right", font=("Verdana", 10, "normal"))
